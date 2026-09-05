import tkinter as tk
import random
# pyright: reportUnusedImport=false
# import gpiozero  # type: ignore[import-not-found]

# led = gpiozero.LED(17)

num = 0

def change_text():
    global num
    
    #phrases = (num)
    # Update the StringVar with a random phrase
    text_var.set(num)
    num = num + 10

root = tk.Tk()
root.title("Dynamic Button Update")
root.geometry("600x300")

# Create the StringVar
text_var = tk.StringVar()
text_var.set(num)

# Link StringVar to the Label
label = tk.Label(root, textvariable=text_var, font=("Arial", 24), wraplength=250)
label.pack(pady=50)

# Button triggers the update function
button = tk.Button(root, text="Update Player 1", command=change_text)
button.pack(pady=10)

num = num + 10

root.mainloop()
