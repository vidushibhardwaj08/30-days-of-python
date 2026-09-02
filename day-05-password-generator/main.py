import random

print("\nPASSWORD GENERATOR\n")
while True:
    password=""
    try:
        length=int(input("Enter password length(more than 4): "))
        if length<4:
            print("please enter a number more than minimum length")
            continue
    except ValueError:
        print("Not a number")
        continue
    characters=[("abcdefghijklmnopqrstuvwxyz"),("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),("1234567890"),("@#_")]

    i=0
    while len(password)<length:
        if i>3:
            i=0
        password= password+random.choice(characters[i])
        i=i+1
    else:
        break

if password!="":
    pass_list = list(password)
    random.shuffle(pass_list)
    new_password="".join(pass_list)
    print(new_password)
