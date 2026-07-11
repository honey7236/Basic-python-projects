# | 2  | 🎯 Number Guessing Game   | `random`, loops, conditions               |

from random import randint

computer = int(randint(1,100))
user = 0
score = 0

print("There is a hidden number guese what is that number.")
user = int(input("Enter a number : "))

while computer != user:
    if computer > user:
        score += 1
        print("guess a grater number.")
        user = int(input("Enter a number : "))

    elif computer < user:
        score += 1
        print("guess a smaller number.")
        user = int(input("Enter a number : "))

else:
    print(f"congratulations you win the game, the number is {computer}")
    print(f"The attempts you do for guese the number is : {score}")