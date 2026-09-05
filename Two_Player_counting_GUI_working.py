import tkinter as tk
import random
# pyright: reportUnusedImport=false
# import gpiozero  # type: ignore[import-not-found]

# led = gpiozero.LED(17)

num = 00
num2 = 00

def change_text():
    global num
    text_var.set(num)
    num = num + 100

def change_text2():
    global num2
    text_var2.set(num2)
    num2 = num2 + 100

root = tk.Tk()
root.title("Dynamic Button Update")
root.geometry("1200x500")

# Create the StringVar
text_var = tk.StringVar()
text_var.set(num)

text_var2 = tk.StringVar()
text_var2.set(num2)

labelp1 = tk.Label(root, text="Player 1 Score", font=("Arial", 48), wraplength=500)
labelp1.grid(row=0, column=0, padx=80, pady=30)

labelp2 = tk.Label(root, text="Player 2 Score", font=("Arial", 48), wraplength=500)
labelp2.grid(row=0, column=2, padx=80, pady=30)

# Link StringVar to the Label
label = tk.Label(root, textvariable=text_var, font=("Arial", 96), wraplength=750)
label.grid(row=1, column=0, padx=80, pady=30)

# Button triggers the update function
button = tk.Button(root, text="  Update Player 1   ", command=change_text)
button.grid(row=2, column=0, padx=80, pady=10)

label2 = tk.Label(root, textvariable=text_var2, font=("Arial", 96), wraplength=750)
label2.grid(row=1, column=2, padx=80, pady=30)

button2 = tk.Button(root, text="  Update Player 2   ", command=change_text2)
button2.grid(row=2, column=2, padx=80, pady=10)

num = num + 100
num2 = num2 + 100

root.mainloop()
