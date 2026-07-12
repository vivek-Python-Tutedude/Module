
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


user_input = tk.Entry(width=50,)
user_input.pack()

button = tk.Button(text="Click",command = fun_button)
button.pack()

destory_button = tk.Button(text = "Click for destroy!!", command=window.destroy )
destory_button.pack()
# window.destroy is used for terminate the pop up window and it will exit the code
window.mainloop()