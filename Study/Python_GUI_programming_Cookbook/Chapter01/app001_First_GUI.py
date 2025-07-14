# app001.py
# import 

import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# add a title
win.title("Python GUI")

# Adding a Label
ttk.Label(win, text="A Label").grid(column=0, row=0)

# Start GUI
win.mainloop()
