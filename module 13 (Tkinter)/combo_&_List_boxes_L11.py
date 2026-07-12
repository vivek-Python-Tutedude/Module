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
# You have to see the value in terminal when you select the option  mala or female


# combo boxes ==> it will allows the users to select one value from the drop down

"""
selected_contry = tk.StringVar()
countries = ttk.Combobox(textvariable=selected_contry, values=("Australia", "Canada", "India","Sweden", "US"))
countries.pack()
# with the help of that we can create a drop down and select the values as per given 
# in above if state is not define then we can write our own values inside that drop down 
# for example above code
"""
"""
selected_contry = tk.StringVar()
countries = ttk.Combobox(textvariable=selected_contry, values=("Australia", "Canada", "India","Sweden", "US"))
countries["state"] = "readonly"
countries.pack()
# with the help of that we can create a drop down and select the values as per given 
# in above if state is define as "readonly" then we can not write our own values inside that drop down 
# for example above code

"""
"""
selected_contry = tk.StringVar()
countries = ttk.Combobox(textvariable=selected_contry, values=("Australia", "Canada", "India","Sweden", "US"))
countries["state"] = "readonly"
countries.pack()

def display_country(event): # passing the one parameter event
    print(f"Selected Country is {selected_contry.get()}")

countries.bind("<<ComboboxSelected>>", display_country) # the parameter is passed from here
# we are fetch the value see in terminal we can get the selected contry printed from the drop down
"""
"""
selected_contry = tk.StringVar()
countries = ttk.Combobox(textvariable=selected_contry, values=("Australia", "Canada", "India","Sweden", "US"))
countries["state"] = "readonly"
countries.pack()

def display_country(event): # passing the one parameter event
    msg = f"selected country is {selected_contry.get()}"
    country_lable = tk.Label(text = msg, font=custom_font)
    country_lable.pack()

countries.bind("<<ComboboxSelected>>", display_country)
"""
# in this we are printing the selected country on the pop up window



# List box ==> in this also we have to choose the mutiple options
# but we can see all the options at once it's not a drop down
# it kind of box where in all the options can be seen depending on how we cofigure it
# in this there is the option of selecting the multiple option(more than option)

"""
food_items = ("Pizza", "Burger", "Garlic bread", "Nachos", "salad")
fav_food = tk.StringVar(value=food_items)

food_list = tk.Listbox(listvariable=fav_food, height=5)
food_list.pack()
# we can select only one option in this code
"""

"""
food_items = ("Pizza", "Burger", "Garlic bread", "Nachos", "salad")
fav_food = tk.StringVar(value=food_items)

food_list = tk.Listbox(listvariable=fav_food, height=5, selectmode="extended")
food_list.pack()
# we can select mutiple option in this code
# for selecting mutiple values use Ctrl + mouse click
"""

"""
food_items = ("Pizza", "Burger", "Garlic bread", "Nachos", "salad")
fav_food = tk.StringVar(value=food_items)

food_list = tk.Listbox(listvariable=fav_food, height=5, selectmode="extended")
food_list.pack()

def get_fav_food(event): # passing the one parameter event
    print(fav_food.get())

food_list.bind("<<ListboxSelect>>", get_fav_food)
# in this code we will get all the valuse  inside the tuple insted of fav_food
"""
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
window.mainloop()
