# app002_GUI_not_resizable.py

# imports
import tkinter as tk

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# Disable resizing the GUI by passing in FAlse/False
win.resizable(False, False)

# Enable resizing x-dimention, disable y-dimension
# win.resizable(True, False)

# Start GUI
win.mainloop()
