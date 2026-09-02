import random

print("\nPASSWORD GENERATOR\n")

try:
    length=int(input("Enter password length: "))
except ValueError:
    print("Not a number")
    exit()
characters=[("abcdefghijklmnopqrstuvwxyz"),("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),("1234567890"),("@#_")]

password=""
while len(password)<length:
    i= random.randint(0,3)
    password= password+random.choice(characters[i])

print(password)
