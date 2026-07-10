# | 1  | 🧮 Calculator             | Input, operators, functions, `if-else`    |

# Define basic calculator functions for reuse.
# Each function takes two numbers and returns the result.
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

# Welcome message shown when the program starts.
print("This is a calculator you can calculate 2 numbers.")

# Initialize variables for the two numbers.
a = 0
b = 0

# Use an infinite loop so the user can perform many calculations.
while True:

    # Get the two numbers from the user.
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    # Show the menu of available operations.
    print("Press 1 for addition.")
    print("Press 2 for substraction.")
    print("Press 3 for multiplication.")
    print("Press 4 for division.")
    print("Press 5 to exit.")

    # Read the user's choice from the menu.
    choice = int(input("Enter your dision : "))

    # Perform the selected operation and display the result.
    if choice == 1:
        result = add(a, b)
        print(f"The answer is {result}")

    elif choice == 2:
        result = sub(a, b)
        print(f"The answer is {result}")
        
    elif choice == 3:
        result = multi(a, b)
        print(f"The answer is {result}")
        
    elif choice == 4:
        result = div(a, b)
        print(f"The answer is {result}")
    
    # Exit the loop and end the program when the user chooses 5.
    elif choice == 5:
        break

