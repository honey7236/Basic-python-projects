# | ⭐⭐⭐ 3       | **Library Management System**  | Multiple Classes, Composition, Object Relationships   
          
import json
from pathlib import Path
from data import books, members

database = Path('library_data.json')
data = []


if Path(database).exists():             #check if json file exists open the file and load the content in data 
    with open(database,"r") as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():                             #this function can save the data in json file
    with open(database, "w") as f:
        json.dump(data, f, indent=4)

class book:

    def add_book(self):
        book_name = input("enter book name :- ")
        for i in books:
            if i['title'] == book_name:
                print("Book is already in library.")
                return
        
        author_name = input("Enter the author name :- ")
        book_id = input("Enter book id :- ")
        books.append({'title':book_name, 'author': author_name, 'book_id': book_id, 'status': "Available"})
        print("Book added succesfully.")


    def view_all_books(self):
        for i in books:
            print(f"""
Bool name = {i['title']}
Author name = {i['author']}
Book id = {i['book_id']}
Status = {i['status']}
""")


    def check_book_status(self):
        book_name = input("enter book name :- ")
        for i in books:
            if i['title'] == book_name:
                print(f"{i['title']} is {i['status']}")   
                return     
        print("Book is not in library.")


    def check_books(self):
        total_available = 0
        total_unavailable = 0
        for i in books:
            if i['status'] == "Available":
                total_available += 1
            else:
                total_unavailable +=1

        print(f"Total available = {total_available}")
        print(f"Total unavailable = {total_unavailable}")

b = book()


class member:
    total_books = ""
    borrow_books= ""
    def register(self):
        user_name = input("Enter your name :- ")
        member_id = int(input("Enter your member id :- "))
        data.append({'name': user_name, 'member_id': member_id, 'borrowed_books': "", 'total_books': 0})
        save()
        print("User registered succesfully.")


    def borrow_book(self):
        book_name = input("Enter book name :- ")
        member_id = int(input("Enter your member id :- "))
        for i in books:
            if i['title'] == book_name and i['status'] == "Available":
                for j in data:
                    if j['member_id'] == member_id:  
                        self.borrow_books = j['borrowed_books']
                        self.borrow_books += book_name    
                        j['borrowed_books'] = self.borrow_books + ", "
                        i['status'] = "Borrowed"
                        self.total_books = j['total_books']
                        self.total_books += 1
                        j['total_books'] = self.total_books
                        print("Book borrowed succesfully.")
                        save()
                        return


    def return_book(self):
        book_name = input("Enter your name :- ")
        member_id = int(input("Enter your member id :- "))
        for i in books:
            if i['title'] == book_name and i['status'] == "Borrowed":
                for j in data:
                    if j['member_id'] == member_id:
                        j['borrowed_books'] -= book_name
                        i['status'] = "Available"
                        self.total_books = j['total_books']
                        self.total_books -= 1
                        j['total_books'] = self.total_books
                        print("Book retured succesfully.")
                        save()
                        return


    def check_user_details(self):
        member_id = int(input("Enter your user id :- "))
        for i in members:
            if i['member_id'] == member_id:
                print(f"""
                      
Name = {i['name']}
Member id = {i['member_id']}
Borrowed books = {i['borrowed_books']}
Total books = {i['total_books']}

""")

m = member()
    


while True:

    print("""
    Press 1 to Add a book.
    Press 2 to view all book.
    Press 3 to check book status.
    Press 4 to Borrow / Return a book.
    Press 5 to exit.
    """)
    choice = int(input("Enter your choice :- "))

    if choice == 1:
        b.add_book()

    elif choice == 2:
        b.view_all_books()

    elif choice == 3:
        while True:
            print("Press 1 to check a book status.")
            print("Press 2 to check total books status.")
            print("Press 3 to exit.")
            choice = int(input("Enter your choice :- "))
            if choice == 1:
                b.check_book_status()
            elif choice == 2:
                b.check_books()
            elif choice == 3:
                break

    elif choice == 4:
        while True:
            print("Press 1 to register.")
            print("Press 2 to borrow a book.")
            print("Press 3 to return a book.")
            print("Press 4 to check user details.")
            print("Press 5 to exit.")
            choice = int(input("Enter your choice :- "))
            if choice == 1:
                m.register()
            elif choice == 2:
                m.borrow_book()
            elif choice == 3:
                m.return_book()
            elif choice == 4:
                m.check_user_details()
            elif choice == 5:
                break

    elif choice == 5:
        break


