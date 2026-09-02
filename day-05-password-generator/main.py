print("\nPASSWORD GENERATOR\n")

try:
    length=int(input("Enter password length: "))
except ValueError:
    print("Not a number")
    exit()
characters=["abcdefghijklmnopqrstuvwxyz1234567890@#_"]
