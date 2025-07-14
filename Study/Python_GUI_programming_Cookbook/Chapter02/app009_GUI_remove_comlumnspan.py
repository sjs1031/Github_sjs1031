import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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
action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=2, row=1)

# action.configure(state='disabled') # Disable the button widget

# Crating a label and a Combobox
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values']= (1,2,4,42,100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Using a scrolled Text control
scroll_w = 30
scroll_h = 3
scr = scrolledtext.ScrolledText(win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
# scr.grid(column=0, row=5, sticky='WE', columnspan=3)
# scr.grid(column=0, row=5, columnspan=3)
scr.grid(column=0, row=5)

# # Radiobutton Globals
# COLOR1 = 'Blue'
# COLOR2 = 'Gold'
# COLOR3 = 'Red'

# First, We change our Radiobutton global variables in to a list
colors = ["Blue", "Gold", "Red"]

# We have also changed the callback function to ve zero-based, using the list 
# instead of module-level global variables

# # Radiobutton Callback

# def radCall():
#     radSel = radVar.get()
#     if   radSel == 1: win.configure(background=COLOR1)
#     elif radSel == 2: win.configure(background=COLOR2)
#     elif radSel == 3: win.configure(background=COLOR3)

def radCall():
    radSel=radVar.get()
    if   radSel == 0: win.configure(background=colors[0]) # now zero-based
    elif radSel == 1: win.configure(background=colors[1]) # and using list
    elif radSel == 2: win.configure(background=colors[2])


# Create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non=existing index value for radVae
radVar.set(99)

# rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
# rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

# rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)# rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

# rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
# rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

# Now we are creating all three Radiobuton widgets within onel loop
for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# Create a container to hold labels
buttons_frame = ttk.LabelFrame(win, text=' Labels in a Frame')
# buttons_frame.grid(column=1, row=7)
# buttons_frame.grid(column=0, row=7)
# buttons_frame.grid(column=0, row=7, padx=20, pady=20)
buttons_frame.grid(column=0, row=7)

# place labels into the containger element
# ttk.Label(buttons_frame, text="Label1 -- sooooooo much looooonger...").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

name_entered.focus() # Place cursor into name entry

# Start GUI
win.mainloop()
