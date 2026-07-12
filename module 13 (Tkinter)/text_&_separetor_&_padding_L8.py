import tkinter as tk
import tkinter.font as ftk
from tkinter import ttk 
# themed advance version of tkinter
window = tk.Tk()

window.title("My application")
window.minsize(width=500, height=400)

custom_font = ftk.Font(family="Time new roman", size=15, weight="bold")

lable = ttk.Label(text="how are you?", font=custom_font,padding=15) # padding will gives the spaces in both the direction
lable.pack()

def fun():
   lable.config(text=user_input.get())
   
def fun_button():    
    lable.config(text=user_input.get())
    
user_input = ttk.Entry(width=50)
user_input.pack()

Button = ttk.Button(text="Click", width=20, command=fun)
Button.pack()

destory_button = ttk.Button(text = "Click for destroy!!", command=window.destroy )
destory_button.pack()

'''
text = tk.Text()
text.pack()

'''
'''
text = tk.Text(height=5,width=25) # text window size
text.pack()
text.focus() # it gives blking cursor inside the window
text.insert("1.0", "Enter your comment: ") 
# in this 1 = 1st line and 0 = first character stat form both combined used to help in stating position
# text["state"] = "disable" # with the help of that we can't writte the msg inside the window
'''
'''
text = tk.Text(height=5,width=25) # text window size
text.pack()
text.focus() # it gives blking cursor inside the window
text.insert("1.0", "Enter your comment: ") 
text["state"] = "disable"

def enable_text():
    text["state"] = "normal"
    
def disable_text():
    text["state"] = "disable"
    
enable_button = ttk.Button(text="Enable mutiline text box",command=enable_text)
enable_button.pack()

disable_button = ttk.Button(text="Disable mutiline text box",command=disable_text)
disable_button.pack()

'''
'''
text = tk.Text(height=5,width=25) # text window size
text.pack()
text.focus() # it gives blking cursor inside the window
text.insert("1.0", "Enter your comment: ") 
text_data = text.get("1.0", "end")
print(text_data) # check the terminal u see ==> Enter your comment: 

'''
'''
text = tk.Text(height=5,width=25) # text window size
text.pack()
text.focus() # it gives blking cursor inside the window
text.insert("1.0", "Enter your comment: ") 

def text_fun() :
    text_data = text.get("1.0", "end")
    print(text_data) # after running check the terminal

text_button = ttk.Button(text="Featch Text", command=text_fun)
text_button.pack()

'''
"""
'''
sep = ttk.Separator(orient="horizontal") # with help of seperator widget we can put a line or a separator that separates the widgets to understand the window components easily
sep.pack() # defalt size of separetor is 1 pixel so we can;t see the change
'''
sep = ttk.Separator(orient="horizontal") # with help of seperator widget we can put a line or a separator that separates the widgets to understand the window components easily
sep.pack(fill="x") # we can see vertical line between button and entry window

text = tk.Text(height=5,width=25) # text window size
text.pack()
text.focus() # it gives blking cursor inside the window
text.insert("1.0", "Enter your comment: ") 

def text_fun() :
    text_data = text.get("1.0", "end")
    print(text_data) # after running check the terminal

text_button = ttk.Button(text="Featch Text", command=text_fun)
text_button.pack()

"""
sep = ttk.Separator(orient="horizontal") # with help of seperator widget we can put a line or a separator that separates the widgets to understand the window components easily
sep.pack(fill="x") # we can see vertical line between button and entry window

text = tk.Text(height=5,width=25) # text window size
text.pack(padx=20) # padx will give the space in horizantal
text.focus() # it gives blking cursor inside the window
text.insert("1.0", "Enter your comment: ") 

def text_fun() :
    text_data = text.get("1.0", "end")
    print(text_data) # after running check the terminal

text_button = ttk.Button(text="Featch Text", command=text_fun)
text_button.pack(pady=10) # pady will give the space in vertical

window.mainloop()