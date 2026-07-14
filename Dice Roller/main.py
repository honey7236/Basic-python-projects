# | 8  | 🎲 Dice Roller            | Random module, loops                      |

from random import randint

def dice_roll():
    roll = int(randint(1,6))
    print(f"The numbers is {roll}")

while True:
    print('''
    Press 1 to roll the dice.
    Press 2 exit.
    ''')

    choice = int(input("Enter your choice :- "))

    if choice == 1:
        dice_roll()
    elif choice == 2:
        break
    else:
        print("enter a valid input.")