import tkinter as tk
import random


global num
num = 0

def change_text():
    global num
    
    #phrases = (num)
    # Update the StringVar with a random phrase
    text_var.set(num)
    num = num + 1

root = tk.Tk()
root.title("Dynamic Button Update")
root.geometry("300x150")

# Create the StringVar
text_var = tk.StringVar()
text_var.set(num)

# Link StringVar to the Label
label = tk.Label(root, textvariable=text_var, font=("Arial", 14), wraplength=250)
label.pack(pady=20)

# Button triggers the update function
button = tk.Button(root, text="Update Text", command=change_text)
button.pack(pady=10)



root.mainloop()
