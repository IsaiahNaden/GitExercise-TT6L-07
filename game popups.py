import tkinter as tk
from tkinter import messagebox

def ask_question():
    response = messagebox.askyesno("","Do you want to continue the game?")
    if response == "Yes":
        next()

    else :
        exit()

exit1=ask_question()

