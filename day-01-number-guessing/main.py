import random

print("Im thinking of a number between 0 and 100")
actual_number = random.randint(0, 100)

print("You have seven guesses")

count=7

while(count>0):
    guess=int(input("Guess the number"))
    if(guess>0 and guess<100):
        count = count-1
        if(guess<actual_number):
            print("go higher")
        elif(guess>actual_number):
            print("go lower")
        else:
            print("CORRECT!!! YOU WON!!")
            break
    else:
        print("Invalid input")
else:
    print("Game Over")


