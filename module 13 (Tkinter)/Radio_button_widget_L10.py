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

check_option = tk.StringVar() # it is a class StringVar used for string

def check_option_task() :
    print(check_option.get(), type(check_option.get()))
check_button = ttk.Checkbutton(text="Agree with the terms & conditions?", variable=check_option, command=check_option_task, onvalue="Yes", offvalue= "No")
check_button.pack() # look in the terminal if we check print Yes if we uncheck value become No it is in the form of string

# Radio button ==> it is useful to pick between different options 
# These buttons are related to one another and we can choose only  one value from out of these options 

'''
radio_val = tk.StringVar()

option_1 = ttk.Radiobutton(text="Male", variable=radio_val, value='male')
option_1.pack()

option_2 = ttk.Radiobutton(text="Female", variable=radio_val, value='female')
option_2.pack()

'''

def get_radio_value() :
  print(radio_val.get())
    
radio_val = tk.StringVar() # we can use the string value inside the value

option_1 = ttk.Radiobutton(text="Male", variable=radio_val, value='male', command=get_radio_value)
option_1.pack()

option_2 = ttk.Radiobutton(text="Female", variable=radio_val, value='female', command=get_radio_value)
option_2.pack()
# You have to see the value in terminal when you select the option  mala or female

window.mainloop()