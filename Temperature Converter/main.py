# | 5  | 🌡️ Temperature Converter | Functions, arithmetic                     |

print("""
Enter what do you want to do.
Press 1 for celsius to fahrenheit
Press 2 for fahrenheit to celsius
""")

def CelToFer():
    cel = int(input("Enter celsius temprature value : "))
    far = (cel*9/5)+32
    print(f"the fahrenheit value is {far}.")

def FerToCel():
    far = int(input("Enter a fahrenheit temprature value : "))
    cel = (far-32)*5/9
    print(f"The celsius value is {cel}.")

while True:

    choice = int(input("Enter your choice : "))

    if choice == 1:
        CelToFer()
        break

    elif choice == 2:
        FerToCel()
        break

    else:
        print("Enter a valid choice.")
