
import tkinter as tk
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
    

# Taking user input
# class Entry is used for taking the user input
# user_input = tk.Entry()

user_input = tk.Entry(width=50,)
user_input.pack()

# get function it will return current string of user input
#  print(user_input.get()) # we cant print the user input like that 

button = tk.Button(text="Click",command = fun_button)
button.pack()

window.mainloop()