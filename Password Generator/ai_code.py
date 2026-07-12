import random
from random import randint

alphabets = 'abcdefghijklmnopqrstuvwxyz'
alphabets_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_chars = '!@#$%^&*()-_=+[]{}\\|;:\'",.<>/?`~'
numbers = '0123456789'

def generate_password(length=None):
    if length is None:
        length = randint(8, 16)
    
    password_chars = []
    char_pools = [alphabets, alphabets_upper, special_chars, numbers]
    
    for i in range(length):
        pool = random.choice(char_pools)
        password_chars.append(random.choice(pool))
    
    return ''.join(password_chars)

print(generate_password())