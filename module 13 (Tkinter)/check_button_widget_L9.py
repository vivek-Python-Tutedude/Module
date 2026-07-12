import tkinter as tk
from tkinter import ttk 
import tkinter.font as ftk

window = tk.Tk()
window.title("Vivek")
window.minsize(width=400, height=300)

# Font class used to select the font, size of font etc

custom_font = ftk.Font(family="Time New Roman", size= 20, weight="bold", slant="italic")

lable = tk.Label(text = "Vivek Hii !", font=custom_font)
lable.pack()

def fun_button():    
    lable.config(text=user_input.get())


user_input = tk.Entry(width=50,)
user_input.pack()

button = tk.Button(text="Click",command = fun_button)
button.pack()

destory_button = tk.Button(text = "Click for destroy!!", command=window.destroy )
destory_button.pack()

'''
# check button ==> it is similar to labels and buttons basically they're combined together
# it have also a extra options it can check or uncheck the button depending on the requrement 
# it will perform a certain task when the unchek or check are happen 

check_button = ttk.Checkbutton(text="Agree with the terms & conditions?")
check_button.pack()
'''
'''
check_option = tk.IntVar() # it is a class IntVar used fir integer

def check_option_task() :
    print(check_option.get())
check_button = ttk.Checkbutton(text="Agree with the terms & conditions?", variable=check_option, command=check_option_task)
check_button.pack()
# look in the terminal if we check print 1 if we uncheck value become 0 value is in the form of int
'''

''' 
check_option = tk.StringVar() # it is a class StringVar used for string

def check_option_task() :
    print(check_option.get(), type(check_option.get()))
check_button = ttk.Checkbutton(text="Agree with the terms & conditions?", variable=check_option, command=check_option_task)
check_button.pack() # look in the terminal if we check print 1 if we uncheck value become 0 it is in the form of string

'''

'''
check_option = tk.StringVar() # it is a class StringVar used for string

def check_option_task() :
    print(check_option.get(), type(check_option.get()))
check_button = ttk.Checkbutton(text="Agree with the terms & conditions?", variable=check_option, command=check_option_task, onvalue="Yes", offvalue= "No")
check_button.pack() # look in the terminal if we check print Yes if we uncheck value become No it is in the form of string

'''
check_option = tk.BooleanVar() # it is a class StringVar used for string

def check_option_task() :
    print(check_option.get(), type(check_option.get()))
check_button = ttk.Checkbutton(text="Agree with the terms & conditions?", variable=check_option, 
                               command=check_option_task, onvalue="True", offvalue= "False")
check_button.pack() # look in the terminal if we check print Yes if we uncheck value become No it is in the form of string


window.mainloop()