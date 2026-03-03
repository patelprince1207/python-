import random
import string

def Generate_Password(num):
    password = ""
    for _ in range(num):
        password += random.choice(string.digits)   # Only numbers
    return password

print(Generate_Password(6))   # Generate a 6-digit password