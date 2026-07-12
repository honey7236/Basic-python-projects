# | 6  | 📋 To-Do List             | Lists, loops, CRUD operations             |

from pathlib import Path
import os


def create_list():
    try:
        name = input("Enter to do list name :- ")
        path = Path(name)
        if not path.exists():
            with open(path, "w")as fs:
                data = input("Enter your tasks :- ")
                fs.write(data + "\n")
            while True:
                print("Press 1 to add task."
                    "Press 2 to save file.")            
                choice = int(input("Enter your disigion :- "))
                if choice == 1:
                    with open(path, "a")as fs:
                        data = input("Enter your tasks :- ")
                        fs.write(data + "\n")
                else:
                    print("file created succesfully.")
                    break
        else:
            print("Error the file is already existes.")
    except Exception as e:
        print(f"There is an error {e}")


def read_list():
    try:
        name = input("Enter your list name :- ")
        path = Path(name)
        if path.exists():
            with open(path, "r") as fs:
                content = fs.read()
                print(f"here is your to do list : \n{content}")
        else:
            print("file dose not exists.")

    except Exception as e:
        print(f"There is an error {e}")


def update_list():
    try:
        name = input("Enter your list name :- ")
        path = Path(name)
        if path.exists():
            while True:
                print("Press 1 to add task."
                    "Press 2 to save file.")            
                choice = int(input("Enter your disigion :- "))
                if choice == 1:
                    with open(path, "a")as fs:
                        data = input("Enter your tasks :- ")
                        fs.write(data + "\n")
                else:
                    print("file created succesfully.")
                    break

        else:
            print("file dose not exists.")

    except Exception as e:
        print(f"There is an error {e}")


def delete_list():
    try:
        name = input("enter your file name : ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("file deleted succesfully")
        else:
            print("error no such file exists")
    except Exception as err:
        print(f"an error accures as {err}")


while True:

    print("""
    ------To-Do-List-------
        
    Press 1 to create a TDL.
    Press 2 to read a TDL.
    Press 3 to update a TDL.
    Press 4 to delete a TDL.
    Press 5 to exit from TDL.
    
    """)

    choice = int(input("Enter your choice :- "))

    if choice == 1:
        create_list()
    elif choice == 2:
        read_list()
    elif choice == 3:
        update_list()
    elif choice == 4:
        delete_list()
    elif choice == 5:
        break

