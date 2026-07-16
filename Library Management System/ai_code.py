# Library Management System

import json
from pathlib import Path

DATABASE = Path('library_data.json')


class Book:
    """Represents a book in the library."""
    def __init__(self, title, author, book_id, status="Available"):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.status = status

    def to_dict(self):
        """Converts the Book object to a dictionary for JSON serialization."""
        return {
            "title": self.title,
            "author": self.author,
            "book_id": self.book_id,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Book object from a dictionary."""
        return cls(
            title=data["title"],
            author=data["author"],
            book_id=data["book_id"],
            status=data.get("status", "Available")
        )


class Member:
    """Represents a library member."""
    def __init__(self, name, member_id, borrowed_books=None, total_books=0):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
        self.total_books = total_books

    def to_dict(self):
        """Converts the Member object to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books,
            "total_books": self.total_books
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Member object from a dictionary."""
        return cls(
            name=data["name"],
            member_id=data["member_id"],
            borrowed_books=data.get("borrowed_books", []),
            total_books=data.get("total_books", 0)
        )


class Library:
    """Manages the books and members, and controls data persistence."""
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def load_data(self):
        """Loads data from the JSON file, handling missing files and format migrations."""
        if not DATABASE.exists() or DATABASE.stat().st_size == 0:
            self.initialize_default_data()
            return

        try:
            with open(DATABASE, "r") as f:
                raw_data = json.load(f)

            # Check if it is the old list-based format of members
            if isinstance(raw_data, list):
                self.migrate_old_format(raw_data)
                return

            # Check if it is the correct dictionary-based format
            if isinstance(raw_data, dict):
                books_list = raw_data.get("books", [])
                members_list = raw_data.get("members", [])

                self.books = [Book.from_dict(b) for b in books_list]
                self.members = [Member.from_dict(m) for m in members_list]

                # Make sure borrowed_books is a list for all loaded members
                for m in self.members:
                    if isinstance(m.borrowed_books, str):
                        m.borrowed_books = [b.strip() for b in m.borrowed_books.split(",") if b.strip()]
                        m.total_books = len(m.borrowed_books)
                return

        except Exception as e:
            print(f"Error loading JSON data: {e}. Reinitializing database.")
            self.initialize_default_data()

    def initialize_default_data(self):
        """Initializes the database with default books from data.py if available."""
        try:
            from data import books as default_books
            self.books = [Book.from_dict(b) for b in default_books]
        except ImportError:
            self.books = []
        self.members = []
        self.save_to_json()

    def migrate_old_format(self, raw_members):
        """Migrates older member-only JSON list format to the unified JSON dictionary format."""
        parsed_members = []
        for m_dict in raw_members:
            borrowed_val = m_dict.get("borrowed_books", [])
            if isinstance(borrowed_val, str):
                borrowed_list = [b.strip() for b in borrowed_val.split(",") if b.strip()]
            else:
                borrowed_list = list(borrowed_val) if borrowed_val else []

            parsed_members.append(Member(
                name=m_dict.get("name", "Unknown"),
                member_id=m_dict.get("member_id", 0),
                borrowed_books=borrowed_list,
                total_books=len(borrowed_list)
            ))

        # Import books from data.py to merge
        try:
            from data import books as default_books
            self.books = [Book.from_dict(b) for b in default_books]
        except ImportError:
            self.books = []

        # Sync book statuses with migrated members' borrowed books
        borrowed_set = set()
        for m in parsed_members:
            for b_title in m.borrowed_books:
                borrowed_set.add(b_title.lower())

        for b in self.books:
            if b.title.lower() in borrowed_set:
                b.status = "Borrowed"

        self.members = parsed_members
        self.save_to_json()

    def save_to_json(self):
        """Saves current books and members data into the JSON file."""
        data = {
            "books": [b.to_dict() for b in self.books],
            "members": [m.to_dict() for m in self.members]
        }
        with open(DATABASE, "w") as f:
            json.dump(data, f, indent=4)

    def add_book(self):
        """Registers a new book in the library."""
        book_name = input("enter book name :- ")
        
        # Check if a book with this title already exists
        for b in self.books:
            if b.title.lower() == book_name.lower():
                print("Book is already in library.")
                return

        author_name = input("Enter the author name :- ")
        book_id = input("Enter book id :- ")

        # Validate duplicate Book ID
        for b in self.books:
            if b.book_id == book_id:
                print("Error: A book with this ID already exists.")
                return

        new_book = Book(title=book_name, author=author_name, book_id=book_id, status="Available")
        self.books.append(new_book)
        self.save_to_json()
        print("Book added succesfully.")

    def view_all_books(self):
        """Displays all books in the library."""
        if not self.books:
            print("No books available in the library.")
            return
        for b in self.books:
            print(f"""
Book name = {b.title}
Author name = {b.author}
Book id = {b.book_id}
Status = {b.status}
""")

    def check_book_status(self):
        """Checks status of a specific book by name."""
        book_name = input("enter book name :- ")
        for b in self.books:
            if b.title.lower() == book_name.lower():
                print(f"{b.title} is {b.status}")
                return
        print("Book is not in library.")

    def check_books(self):
        """Displays count of total available and unavailable books."""
        total_available = 0
        total_unavailable = 0
        for b in self.books:
            if b.status == "Available":
                total_available += 1
            else:
                total_unavailable += 1

        print(f"Total available = {total_available}")
        print(f"Total unavailable = {total_unavailable}")

    def register(self):
        """Registers a new library member."""
        user_name = input("Enter your name :- ")
        try:
            member_id = int(input("Enter your member id :- "))
        except ValueError:
            print("Error: Member ID must be an integer.")
            return

        # Check for duplicate member ID
        for m in self.members:
            if m.member_id == member_id:
                print("Error: Member ID is already registered.")
                return

        new_member = Member(name=user_name, member_id=member_id)
        self.members.append(new_member)
        self.save_to_json()
        print("User registered succesfully.")

    def borrow_book(self):
        """Enables a member to borrow a book."""
        book_name = input("Enter book name :- ")
        try:
            member_id = int(input("Enter your member id :- "))
        except ValueError:
            print("Error: Member ID must be an integer.")
            return

        # Find the member
        target_member = None
        for m in self.members:
            if m.member_id == member_id:
                target_member = m
                break

        if not target_member:
            print("Error: Member not found.")
            return

        # Validate borrow limit (max 3 books)
        if len(target_member.borrowed_books) >= 3:
            print("Error: Member has already borrowed the limit of 3 books.")
            return

        # Find the book
        target_book = None
        for b in self.books:
            if b.title.lower() == book_name.lower():
                target_book = b
                break

        if not target_book:
            print("Error: Book not found in library.")
            return

        # Validate book availability
        if target_book.status != "Available":
            print(f"Error: '{target_book.title}' is currently unavailable (Status: {target_book.status}).")
            return

        # Update status and user record
        target_book.status = "Borrowed"
        target_member.borrowed_books.append(target_book.title)
        target_member.total_books = len(target_member.borrowed_books)

        self.save_to_json()
        print("Book borrowed succesfully.")

    def return_book(self):
        """Enables a member to return a borrowed book."""
        book_name = input("Enter book name :- ")
        try:
            member_id = int(input("Enter your member id :- "))
        except ValueError:
            print("Error: Member ID must be an integer.")
            return

        # Find the member
        target_member = None
        for m in self.members:
            if m.member_id == member_id:
                target_member = m
                break

        if not target_member:
            print("Error: Member not found.")
            return

        # Verify book was borrowed by the member
        borrowed_book_title = None
        for title in target_member.borrowed_books:
            if title.lower() == book_name.lower():
                borrowed_book_title = title
                break

        if not borrowed_book_title:
            print("Error: This member did not borrow a book with that name.")
            return

        # Find book in library list to reset status
        target_book = None
        for b in self.books:
            if b.title.lower() == book_name.lower():
                target_book = b
                break

        if target_book:
            target_book.status = "Available"

        # Update member record
        target_member.borrowed_books.remove(borrowed_book_title)
        target_member.total_books = len(target_member.borrowed_books)

        self.save_to_json()
        print("Book retured succesfully.")

    def check_user_details(self):
        """Displays registration details and borrowed books of a member."""
        try:
            member_id = int(input("Enter your user id :- "))
        except ValueError:
            print("Error: Member ID must be an integer.")
            return

        for m in self.members:
            if m.member_id == member_id:
                borrowed_str = ", ".join(m.borrowed_books) if m.borrowed_books else "None"
                print(f"""
Name = {m.name}
Member id = {m.member_id}
Borrowed books = {borrowed_str}
Total books = {m.total_books}
""")
                return
        print("Error: Member not found.")


# Entry point menu loop
if __name__ == "__main__":
    library = Library()

    while True:
        print("""
    Press 1 to Add a book.
    Press 2 to view all book.
    Press 3 to check book status.
    Press 4 to Borrow / Return a book.
    Press 5 to exit.
    """)
        try:
            choice = int(input("Enter your choice :- "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if choice == 1:
            library.add_book()

        elif choice == 2:
            library.view_all_books()

        elif choice == 3:
            while True:
                print("Press 1 to check a book status.")
                print("Press 2 to check total books status.")
                print("Press 3 to exit.")
                try:
                    sub_choice = int(input("Enter your choice :- "))
                except ValueError:
                    print("Error: Please enter a valid number.")
                    continue

                if sub_choice == 1:
                    library.check_book_status()
                elif sub_choice == 2:
                    library.check_books()
                elif sub_choice == 3:
                    break
                else:
                    print("Error: Invalid choice.")

        elif choice == 4:
            while True:
                print("Press 1 to register.")
                print("Press 2 to borrow a book.")
                print("Press 3 to return a book.")
                print("Press 4 to check user details.")
                print("Press 5 to exit.")
                try:
                    sub_choice = int(input("Enter your choice :- "))
                except ValueError:
                    print("Error: Please enter a valid number.")
                    continue

                if sub_choice == 1:
                    library.register()
                elif sub_choice == 2:
                    library.borrow_book()
                elif sub_choice == 3:
                    library.return_book()
                elif sub_choice == 4:
                    library.check_user_details()
                elif sub_choice == 5:
                    break
                else:
                    print("Error: Invalid choice.")

        elif choice == 5:
            print("Exiting Library. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select between 1 and 5.")
