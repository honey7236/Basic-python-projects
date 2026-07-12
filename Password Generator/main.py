# | 4  | 🔑 Password Generator     | Strings, loops, `random`, `string` module |

#A basic password needs min 8 characters + num + special character + uppercase 
# random.choice(my_list)

import random
from random import randint

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

alphabets_upper = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]

special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+', '[', ']',
    '{', '}', '\\', '|', ';', ':', "'", '"',
    ',', '.', '<', '>', '/', '?', '`', '~'
]

numbers = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]

password = ""

def ran_char():
    global password
    password += str(random.choice(alphabets))
def ran_char_up():
    global password
    password += str(random.choice(alphabets_upper))
def ran_special():
    global password
    password += str(random.choice(special_chars))
def ran_num():
    global password
    password += str(random.choice(numbers))

function_list = [ran_char, ran_char_up, ran_special, ran_num]

l = int(randint(8,16))

for i in range(l):
    chosen_func = random.choice(function_list)
    chosen_func()

print(password)
