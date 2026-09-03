import tkinter as tk
import random

def roll_die():
    x= random.randint(1,6)
    result_label.config(text=f"You rolled: {x}")

root = tk.Tk()
root.title("Let's roll")

label = tk.Label(
    root, 
    text="DICE ROLLING SIMULATOR",
    font=("Arial",15)
    )
label.pack()

result_label = tk.Label(
    root,
    text="Click Roll Dice!"
)

result_label.pack()

button = tk.Button(root, text="Roll Dice", command=roll_die)
button.pack()

root.mainloop()

