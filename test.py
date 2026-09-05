import tkinter as tk

# 1. Create the main application window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

# 2. Create a widget (a simple label)
label = tk.Label(root, text="Hello, World!", font=("Arial", 14))

# 3. Position the widget using a geometry manager
label.pack(pady=20)

# 4. Start the event loop (keeps the window open and active)
root.mainloop()
