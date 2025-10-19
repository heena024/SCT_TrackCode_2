import tkinter as tk
import random
from tkinter import messagebox


number_to_guess = random.randint(1, 100)


def check_guess():
    guess = int(entry.get())
    if guess < number_to_guess:
        messagebox.showinfo("Result", "Too low! Try again.")
    elif guess > number_to_guess:
        messagebox.showinfo("Result", "Too high! Try again.")
    else:
        messagebox.showinfo("Result", "🎉 Correct! You guessed the number!")


window = tk.Tk()
window.title("Guess the Number")

label = tk.Label(window, text="Guess a number between 1 and 100:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

button = tk.Button(window, text="Check", command=check_guess)
button.pack(pady=10)

window.mainloop()
