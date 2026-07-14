from pathlib import Path

def create_file():
    try:
        name = input("Enter file name:- ")
        path = Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data = input("Enter a note :- ")
                fs.write(data)
            print("File created successfully.")
        else:
            print("file is already exists.")
    except Exception as e:
        print(f"there is an error {e}")


def read_file():
    try:
        name = input("Enter file name:- ")
        path = Path(name)
        if path.exists():
            with open(path,"r") as fs:
                data = fs.read()
                print("\n", data)
        else:
            print("File is not exists.")
    except Exception as e:
        print(f"there is an error {e}")

def update_file():
    try:
        name = input("Enter file name:- ")
        path = Path(name)
        if path.exists():
            print("press 1 to append the file.")
            print("press 2 to overwrite the file.")
            choice = int(input("Enter your choice :- "))
            if choice == 1:
                with open(path, "a") as fs:
                    data = input("Enter what you want to append :- ")
                    fs.write("\n" + data)
                print("append succesfully.")
            elif choice == 2:
                with open(path,"w") as fs:
                    data = input("Enter a note :- ")
                    fs.write(data)
                print("File overwrite successfully.")
        else:
            print("file not exits.")
    except Exception as e:
        print(f"there is an error {e}")
        
def delete_file():
    try:
        name = input("Enter file name:- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("file deleted succesfully")
        else:
            print("error no such file exists")
    except Exception as e:
        print(f"there is an error {e}")



print("Press 1 to create a note.")
print("Press 2 to read a note.")
print("Press 3 to update a note.")
print("Press 4 to delete a note.")

choice = int(input("Enter your choice :- "))

if choice == 1:
    create_file()
elif choice == 2:
    read_file()
elif choice == 3:
    update_file()
elif choice == 4:
    delete_file()
