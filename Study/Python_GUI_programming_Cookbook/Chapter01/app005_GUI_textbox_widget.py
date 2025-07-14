import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# add a title
win.title("Python GUI")

# Button Click Event Function
def click_me():
    action.configure(text='Hello ' +name.get())

# Changing our label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Text box Entry widget
name=tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a button
action = ttk.Button(win, text="Click me", command=click_me)
action.grid(column=1, row=1)

# Start GUI
win.mainloop()
