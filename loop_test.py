import tkinter as tk

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Tkinter Loop Example")
root.geometry("600x300")

# Setup variables and widgets
counter = 0
label = tk.Label(root, text="Loop iterations: 0", font=("Arial", 14))
label.pack(pady=20)

num = 00

def change_text():
    global num
    
    num = num + 100


def my_loop():
    global counter
    counter += 1
    
    # 1. Perform your periodic logic here
    label.config(text=f"Loop iterations: {counter}")

    button = tk.Button(root, text="  Update Player 1   ", command=change_text)
    
    # 2. Schedule this same function to run again after 1000ms (1 second)
    root.after(1000, my_loop)



# Start the repeating cycle by calling it manually once
my_loop()

# Enter Tkinter's necessary event loop
root.mainloop()
