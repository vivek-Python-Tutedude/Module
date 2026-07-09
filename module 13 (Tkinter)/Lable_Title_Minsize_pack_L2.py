"""
import tkinter as tk

window = tk.Tk()
window.title("Vivek")

'''
lable = tk.Label(text = "Hello World!") # class Lable is used to give the text inside the window
lable.pack() # pack method is uesd to impement the labal so it will apper on display 
#             and it will resize the window size automatically as per the text

'''

lable = tk.Label(text = "Hello World! \n \n Have a nice day! ")
lable.pack()
window.mainloop()

"""
"""
import tkinter as tk

window = tk.Tk()
window.title("Vivek")
window.minsize(width=400, height=300) # manually give size to windows
# if content is not in that given size so size automatically adjust and also we can manually resize the window

lable = tk.Label(text = "Hello World! \n \n Have a nice day!", font=("italic", 15, "bold")) 
# in Lable class there is an argument font it will accept the tuple with the help of that we can change the font
lable.pack()
window.mainloop()

"""
"""
import tkinter as tk
import tkinter.font as ftk

window = tk.Tk()
window.title("Vivek")
window.minsize(width=400, height=300)

# Font class used to select the font, size of font etc
# custom_font = ftk.Font(family="Time New Roman", size= 20, weight="bold")
custom_font = ftk.Font(family="Time New Roman", size= 20, weight="bold", slant="italic")

lable = tk.Label(text = "Hello World! \n \n Have a nice day!", font=custom_font)
lable.pack()
window.mainloop()

"""
"""
import tkinter as tk
import tkinter.font as ftk

window = tk.Tk()
window.title("Vivek")
window.minsize(width=400, height=300)

lable = tk.Label(text = "Hello World! \n \n Have a nice day!")
lable.pack()
lable.config(font=("courier new", 25 ,"underline"))
window.mainloop()

"""

import tkinter as tk
import tkinter.font as ftk

window = tk.Tk()
window.title("Vivek")
window.minsize(width=400, height=300)

lable = tk.Label(text = "Hello World!")
lable.pack() # by default value is top
lable.pack(side="left") 
lable.pack(side="right")
lable.pack(side="bottom")
lable.pack(expand=True) # it will put the text in the middle

lable.config(font=("courier new", 25 ,"underline"))
window.mainloop()