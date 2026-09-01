import random

play='y'
while play=='y' or play=='Y':

    print("Im thinking of a number between 0 and 10")
    actual_number = random.randint(0, 10)
    print("You have 4 guesses")

    count=4

    while count > 0:
        try: 
            guess=int(input("Guess the number: "))
        except ValueError:
            print("Not a valid number")
            continue
        if guess >=0 and guess <=10 :
            count -= 1
            if guess < actual_number :
                print("go higher")
            elif guess > actual_number :
                print("go lower")
            else:
                print("CORRECT!!! YOU WON!!")
                # count=0
                break
            print(f"\nRemaining guess: {count}/7")
        else:
            print("Invalid input")
       
    else:
        print("Game Over")

    play=input("Press 'y' to play again: ")

print("Thanks for playing")



