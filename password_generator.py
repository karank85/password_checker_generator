import tkinter as tk
from tkinter.font import Font
import random
import time

root = tk.Tk()

# Customise the size of the interface
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()



bigFont = Font(
    family="Arial",
    size=42,
    underline=1,
    weight="bold",
)

#Creating title
titleLabel = tk.Label(root, text="Password Generator/Checker", font=bigFont, justify="left",pady=20)
titleLabel.pack()




def generatePassword():
    length_number = random.randint(6, 12)
    all_options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$#@%!"
    password = ""
    index = 0
    while index < length_number:
        random_index = random.randint(0, len(all_options)-1)
        password += all_options[random_index]
        index += 1
    if conditions(password):
        myLabel['text'] = password
    else:
        generatePassword()



def checkPassword():
    password = entry.get()
    verdict = conditions(password)
    if verdict:
        myLabel['text'] = f"Good password: {password}"

    else:
        myLabel['text'] = f"Bad password: {password}"


def conditions(password):
    st_password = set(password)
    length_condition = len(password) <= 12 and len(password) >= 6
    lower_case = len(st_password & set("abcdefghijklmnopqrstuvwxyz")) >= 1
    upper_case = len(st_password & set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) >= 1
    special_symbol = len(st_password & set("$#@%!")) >= 1
    repeat_three = threeRepeat(password)
    return length_condition and lower_case and upper_case and special_symbol and repeat_three


def threeRepeat(passwd):
    for i in range(len(passwd) - 2):
        if passwd[i] == passwd[i + 1] == passwd[i + 2]:
            return False
    return True


# Empty label
myLabel = tk.Label(root, text="")
myLabel.pack()

# Making entry box
entry = tk.Entry(root)
entry.pack()

# button for checking the password
button1 = tk.Button(root, text="Check password", command=checkPassword)
button1.pack()

# button for generating the password
button2 = tk.Button(root, text="Generate password", command=generatePassword)
button2.pack()

root.mainloop()
