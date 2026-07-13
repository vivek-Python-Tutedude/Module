"""
Problem Statement: 
Create a Python calculator application using the Tkinter library that provides a graphical user interface (GUI)
for performing basic arithmetic operations

"""

# Import all Tkinter widgets
from tkinter import *

# Create the main window
window = Tk()
window.title("Vivek's Calculator")
window.minsize(width = 400, height = 400)


# Function to display the number clicked on the entry box
def click(num) :
    result = entry.get() # Get current value from entry
    entry.delete(0, END) # Clear the entry box
    entry.insert(0, str(result) + str(num)) # Add the clicked number


# Entry box for displaying numbers and results
entry = Entry(width = 50, borderwidth = 5)
entry.place(x = 0, y = 0)


# Number Buttons

b1 = Button(text = '1', width = 10, command = lambda : click(1))
b1.place(x = 10, y = 50)

b2 = Button(text = '2', width = 10, command = lambda : click(2))
b2.place(x = 100, y = 50)

b3 = Button(text = '3', width = 10, command = lambda : click(3))
b3.place(x = 190, y = 50)

b4 = Button(text = '4', width = 10, command = lambda : click(4))
b4.place(x = 10, y = 100)

b5 = Button(text = '5', width = 10, command = lambda : click(5))
b5.place(x = 100, y = 100)

b6 = Button(text = '6', width = 10, command = lambda : click(6))
b6.place(x = 190, y = 100)

b7 = Button(text = '7', width = 10, command = lambda : click(7))
b7.place(x = 10, y = 150)

b8 = Button(text = '8', width = 10, command = lambda : click(8))
b8.place(x = 100, y = 150)

b9 = Button(text = '9', width = 10, command = lambda : click(9))
b9.place(x = 190, y = 150)

b0 = Button(text = '0', width = 10, command = lambda : click(0))
b0.place(x = 10, y = 200)


# Store the first number and select addition
def add() :
    n1 = entry.get()
    global maths, i
    i = int(n1)
    maths = "add"
    entry.delete(0, END)


badd = Button(text = '+', width = 10, command = add)
badd.place(x = 100, y = 200)


# Store the first number and select subtraction
def sub() :
    n1 = entry.get()
    global maths, i
    i = int(n1)
    maths = "sub"
    entry.delete(0, END)


bsub = Button(text = '-', width = 10, command = sub)
bsub.place(x = 190, y = 200)


# Store the first number and select multiplication
def mul() :
    n1 = entry.get()
    global maths, i
    i = int(n1)
    maths = "mul"
    entry.delete(0, END)


bmul = Button(text = '*', width = 10, command = mul)
bmul.place(x = 10, y = 250)


# Store the first number and select division
def div() :
    n1 = entry.get()
    global maths, i
    i = int(n1)
    maths = "div"
    entry.delete(0, END)


bdiv = Button(text = '/', width = 10, command = div)
bdiv.place(x = 100, y = 250)


# Perform the selected operation and display the result
def eql() :
    n2 = entry.get()
    entry.delete(0, END)

    if maths == "add" :
        entry.insert(0, i + int(n2))

    elif maths == "sub" :
        entry.insert(0, i - int(n2))

    elif maths == "mul" :
        entry.insert(0, i * int(n2))

    elif maths == "div" :
        if int(n2) == 0 :
            entry.insert(0, "Cannot divide by 0")
        else :
            entry.insert(0, i / int(n2))

beql = Button(text = '=', width = 10, command = eql)
beql.place(x = 190, y = 250)


# Clear everything from the entry box
def clr() :
    entry.delete(0, END)


bclr = Button(text = 'Clear', width = 10, command = clr)
bclr.place(x = 10, y = 300)


# Keep the window running
window.mainloop()