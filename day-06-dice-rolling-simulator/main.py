import random

def roll_die():
    x= random.randint(1,6)
    return x

chance = roll_die()
print(chance)