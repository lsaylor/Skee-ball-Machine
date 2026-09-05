import tkinter as tk
import random
# pyright: reportUnusedImport=false
# import gpiozero  # type: ignore[import-not-found]

# led = gpiozero.LED(17)

num = 0
num2 = 0

def change_text():
    global num
    text_var.set(num)
    num = num + 10

def change_text2():
    global num2
    text_var2.set(num2)
    num2 = num2 + 10

root = tk.Tk()
root.title("Dynamic Button Update")
root.geometry("600x300")

# Create the StringVar
text_var = tk.StringVar()
text_var.set(num)

text_var2 = tk.StringVar()
text_var2.set(num2)

# Link StringVar to the Label
label = tk.Label(root, textvariable=text_var, font=("Arial", 24), wraplength=250)
label.pack(pady=20)

# Button triggers the update function
button = tk.Button(root, text="Update Player 1", command=change_text)
button.pack(pady=10)

label2 = tk.Label(root, textvariable=text_var2, font=("Arial", 24), wraplength=250)
label2.pack(pady=20)

button2 = tk.Button(root, text="Update Player 2", command=change_text2)
button2.pack(pady=10)

num = num + 10
num2 = num2 + 10

root.mainloop()
