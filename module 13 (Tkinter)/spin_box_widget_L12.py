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
check_button.pack()

def get_radio_value() :
  print(radio_val.get())
    
radio_val = tk.StringVar() # we can use the string value inside the value

option_1 = ttk.Radiobutton(text="Male", variable=radio_val, value='male', command=get_radio_value)
option_1.pack()

option_2 = ttk.Radiobutton(text="Female", variable=radio_val, value='female', command=get_radio_value)
option_2.pack()

food_items = ("Pizza", "Burger", "Garlic bread", "Nachos", "salad")

fav_food = tk.StringVar(value=food_items)

food_list = tk.Listbox(listvariable=fav_food, height=5, selectmode="extended")
food_list.pack()

def get_fav_food(event): # passing the one parameter event
    food_indices = food_list.curselection() # Return the indices of currently selected item.
    for i in food_indices :
        print(food_list.get(i))

food_list.bind("<<ListboxSelect>>", get_fav_food)
# in this we are printing the selectd value inside the terminal
# in this also we can select mutiple items


# Spin box ==> it is like the counter with up & down arrows to increase or decrease the values

"""
spin_box = ttk.Spinbox(from_= 0, to = 20)
spin_box.pack()
# in this code on pop up window their is a box it count 0 - 20
"""
"""
counter = tk.IntVar(value=10)
spin_box = ttk.Spinbox(from_= 0, to = 20, textvariable=counter)
spin_box.pack()
# in this code on pop up window their is a box it count 0 - 20 but on the box initialy 10 is present
"""
"""
counter = tk.IntVar(value=10)
spin_box = ttk.Spinbox(from_= 0, to = 20, textvariable=counter, wrap=True)
spin_box.pack()
# wrap the default value is zero
# normally if it reaches max limit(20) or reach min limit (0) then we press up or down arrow does not happen anything it will stop
# but when we write wrap = True then after reach max limt it go to the min limt and vice vers 
# it is also called as circular counting
"""
"""
def get_spin_box() :
    print(f"Current spinbox value : {spin_box.get()}")


counter = tk.IntVar(value=10)
spin_box = ttk.Spinbox(from_= 0, to = 20, textvariable=counter, wrap=True, command=get_spin_box)
spin_box.pack()

print(f"Initial spinbox value : {spin_box.get()}")
# in this on the terminal printing the inital and current value 
"""

"""def get_spin_box() :
    print(f"Current spinbox value : {spin_box.get()}")


counter = tk.IntVar(value=10)
spin_box = ttk.Spinbox(values=(10, 15, 30, 60, 00), textvariable=counter, wrap=True, command=get_spin_box)
spin_box.pack()

print(f"Initial spinbox value : {spin_box.get()}")
# in this on the terminal printing the inital and current value as per given
"""
def get_spin_box() :
    print(f"Current spinbox value : {spin_box.get()}")


counter = tk.IntVar(value=10)
spin_box = ttk.Spinbox(values=tuple(range(39, 1000, 100)), textvariable=counter, wrap=True, command=get_spin_box)
spin_box.pack()

print(f"Initial spinbox value : {spin_box.get()}")
# in this on the terminal printing the inital and current value as per given

window.mainloop()