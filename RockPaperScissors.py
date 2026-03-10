import tkinter as tk
import random

def play(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    if user_choice == computer_choice:
        result = "It is a Tie!"

    elif user_choice == "Rock" and computer_choice == "Scissors":
        result = "You Win!"

    elif user_choice == "Paper" and computer_choice == "Rock":
        result = "You Win!"

    elif user_choice == "Scissors" and computer_choice == "Paper":
        result = "You Win!"

    else:
        result = "Computer Wins!"

    label1.config(text="Computer: " + computer_choice)
    label2.config(text=result)

def rock():
    play("Rock")

def paper():
    play("Paper")

def scissors():
    play("Scissors")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

btn1 = tk.Button(root, text="Rock", command=rock)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Paper", command=paper)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Scissors", command=scissors)
btn3.pack(pady=5)

label1 = tk.Label(root, text="")
label1.pack(pady=10)

label2 = tk.Label(root, text="")
label2.pack()

root.mainloop()