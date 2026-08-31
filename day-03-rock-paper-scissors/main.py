import random

options= {1:"rock", 2:"paper", 3:"scissors"}

computer_choice= random.choice(list(options.keys()))
try:
    user_choice= int(input("Choose: \n 1 for ROCK\n 2 for PAPER\n 3 for SCISSORS\n"))
except ValueError:
    print("Invalid User Input")
    exit()

if user_choice not in options:
    print("Choose from the given options")
    exit()

print(f"User chose: {options[user_choice]}")
print(f"Computer chose: {options[computer_choice]}")

if computer_choice==user_choice:
    print("DRAW")
elif computer_choice==1:
    if user_choice==2:
        print("USER WINS")
    else:
        print("COMPUTER WINS")
elif computer_choice==2:
    if user_choice==1:
        print("COMPUTER WINS")
    else:
        print("USER WINS")
elif computer_choice==3:
    if user_choice==1:
        print("USER WINS")
    else:
        print("COMPUTER WINS")