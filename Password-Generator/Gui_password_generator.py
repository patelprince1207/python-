import random
from tkinter import *
import string

def generate_password():
    characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for _ in range(12))
    lbl.config(text=password)

# Main Window
root = Tk()
root.title("Password Generator")
root.geometry("350x250")
root.configure(bg="#1e1e1e")   # Dark background

# Title Label
title = Label(root, text="PASSWORD GENERATOR",
              font=("Arial", 16, "bold"),
              bg="#1e1e1e",
              fg="white")
title.pack(pady=15)

# Generate Button
btn = Button(root,
             text="Generate Password",
             command=generate_password,
             font=("Arial", 12, "bold"),
             bg="#00adb5",
             fg="white",
             activebackground="#008891",
             activeforeground="white",
             relief=FLAT,
             padx=10,
             pady=5)

btn.pack(pady=15)

# Password Output Label
lbl = Label(root,
            text="",
            font=("Consolas", 14, "bold"),
            bg="#1e1e1e",
            fg="#00ffcc")

lbl.pack(pady=20)

root.mainloop()