'''
import tkinter as tk
import tkinter.font as ftk

window = tk.Tk()
window.title("Vivek")
window.minsize(width=400, height=300)

# Font class used to select the font, size of font etc

custom_font = ftk.Font(family="Time New Roman", size= 20, weight="bold", slant="italic")

lable = tk.Label(text = "Hello World!", font=custom_font)
lable.pack()
lable["text"] = "Have a nice day!" # changing the lable text Hello World! to Have a nice day!
# excution is too fast instently changes

# config() method is used to change the parameter of the class lable  parameter like font or text
lable.config(text="Vivek Hii !")# changing the lable text Have a nice day! to vivek Hii!

def fun_button():
    print("Thanks for Clicking")
    
button = tk.Button(text="Click",command = fun_button)
button.pack()

    
window.mainloop()
'''

import tkinter as tk
import tkinter.font as ftk

window = tk.Tk()
window.title("Vivek")
window.minsize(width=400, height=300)

# Font class used to select the font, size of font etc

custom_font = ftk.Font(family="Time New Roman", size= 20, weight="bold", slant="italic")

lable = tk.Label(text = "Hello World!", font=custom_font)
lable.pack()
lable["text"] = "Have a nice day!" # changing the lable text Hello World! to Have a nice day!
# excution is too fast instently changes

# config() method is used to change the parameter of the class lable  parameter like font or text
lable.config(text="Vivek Hii !")# changing the lable text Have a nice day! to vivek Hii!

counter = 0

def fun_button():
    # lable["text"] = "Thanks for clicking"
    global counter
    counter += 1
    lable.config(text=f"Button got cllicked {counter} times!")
    
button = tk.Button(text="Click",command = fun_button)
button.pack()

    
window.mainloop()