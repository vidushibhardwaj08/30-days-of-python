questions={"What is my favorite color":"green", "whats my favorite office character":"kelly", "Whats my favorite number?":5, "What do i like the most?": "reading", "Whats my favorite fruit": "mango"}
options=[("yellow","blue","pink","green"), ("michael","jim","kelly","dwight"),(5,8,7,2),("swimming","reading","singing","dancing"),("banana","apple","mango","litchi")]

x = list(questions.keys())
y = list(questions.values())

i=0
score=0
while i<5:
    print("\n")
    print(f"Question {i+1}:\n{x[i]}")
    print(f"Options are {options[i]}")
    answer= input("your answer: ")
    if answer.lower()==y[i]:
        print("CORRECT\n\n")
        score+=1
        print(f"Current Score: {score}/5")
    else:
        print(f"WRONG ({y[i]} is the correct answer)\n\n")
    i+=1

print(f"\nTotal score: {score}/5")
print("Quiz over")
