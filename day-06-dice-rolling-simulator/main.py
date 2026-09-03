import random

def roll_die():
    x= random.randint(1,6)
    return x

print("DICE ROLLING SIMULATOR")
answer= input("Do you want to roll the dice? (y/n): ")

while answer.lower()=='y':
    result=roll_die()
    print(f"You rolled: {result}")
    answer= input("Do you want to roll the dice? (y/n): ")

print("Thanks for playing!!")
