import tkinter as tk
import tkinter.font as ftk
from tkinter import ttk 
# themed advance version of tkinter
window = tk.Tk()

window.title("My application")
window.minsize(width=500, height=400)

custom_font = ftk.Font(family="Time new roman", size=15, weight="bold")

lable = ttk.Label(text="how are you?", font=custom_font)
lable.pack()

def fun():
   lable.config(text=user_input.get())
    
user_input = ttk.Entry(width=50)
user_input.pack()

Button = ttk.Button(text="Click", width=20, command=fun)
Button.pack()

window.mainloop()