# |  3  | ✂️ Rock-Paper-Scissors    | `if-elif-else`, random module             |

# 1 = rock
# 2 = paper
# 3 = scissor

from random import randint
print('''
 1 = rock
 2 = paper
 3 = scissor
      ''')

user = 2

while True:
    computer = int(randint(1,3))
    user = int(input("Enter your choice : "))

    if user == 1:          #user chose rock
        if computer == 1:
            print(f"computer chose rock")
            print("You chose rock, The match is draw.")
        elif computer == 2:
            print(f"computer chose paper")
            print("You chose rock, you lost.")
            break
        elif computer == 3:
            print(f"computer chose scissor")
            print("You chose rock, you win.")
            break

    elif user == 2:         #user chose paper
        if computer == 1:
            print(f"computer chose rock")
            print("You chose paper, you win")
            break
        elif computer == 2:
            print(f"computer chose paper")
            print("You chose paper, The match is draw.")
        elif computer == 3:
            print(f"computer chose scissor")
            print("You chose paper, you lost.")
            break

    elif user == 3:         #scissor
        if computer == 1:
            print(f"computer chose rock")
            print("you chose scissor, you lost.")
            break
        elif computer == 2:
            print(f"computer chose paper")
            print("you chose scissor, you win.")
            break
        elif computer == 3:
            print(f"computer chose scissor")
            print("you chose scissor, The match is draw.")

