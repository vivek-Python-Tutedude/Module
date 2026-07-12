import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Application")
'''
lable1 = tk.Label(text="vivek", bg = "Red")
lable1.pack()

lable2 = tk.Label(text="Hii", bg = "Green")
lable2.pack()

lable3 = tk.Label(text="How are you", bg="Blue")
lable3.pack()
'''
'''
lable1 = tk.Label(text="vivek", bg = "Red")
lable1.pack(side="left")

lable2 = tk.Label(text="Hii", bg = "Green")
lable2.pack(side="left")

lable3 = tk.Label(text="How are you", bg="Blue")
lable3.pack(side="left")
'''
'''
lable1 = tk.Label(text="vivek", bg = "Red")
# lable1.pack(side="left", fill='y') # fill ='y' mean on y axis (vertical) use all space it does not chane on horizantal side
lable1.pack(side="left", fill='y',expand=True) # because of fill = 'y' it will expand in y dirction (vertically)

lable2 = tk.Label(text="Hii", bg = "Green")
# lable2.pack(side="left", fill='x') # fill ='x' mean on x axis (Horizantal) use all space it does not chane on vertical side
lable2.pack(side="left", fill='x', expand=True) # because of fill = 'x' it will expand in x dirction (Hrizantaly)


lable3 = tk.Label(text="How are you", bg="Blue")
# lable3.pack(side="left",fill='both') # fill= 'both' means use all the space on x and y axis
lable3.pack(side="left",fill='both',expand= True) # it will expand as per the window expands on the foth side becaues of fill = 'both'
'''
'''
lable1 = tk.Label(text="vivek", bg = "Red") 
lable1.pack(side="left",fill= "both",expand=True) 

lable2 = tk.Label(window,text="Hii", bg = "Green")
lable2.pack(side="left", fill='both', expand=True) 

lable3 = tk.Label(text="How are you", bg="Blue")
lable3.pack(side="left",fill='both',expand= True)
'''
# frame ==> It gives us a separet sub window inside the main window so we can use that space separetly
'''
my_frame = ttk.Frame()
my_frame.pack()# does not change anything

lable1 = tk.Label(text="vivek", bg = "Red") 
lable1.pack(side="left",fill= "both",expand=True) 

lable2 = tk.Label(window,text="Hii", bg = "Green")
lable2.pack(side="left", fill='both', expand=True) 

lable3 = tk.Label(text="How are you", bg="Blue")
lable3.pack(side="left",fill='both',expand= True) 
'''
'''
my_frame = ttk.Frame()
my_frame.pack(side="left", fill="both",expand=True) # on left side space is created

lable1 = tk.Label(text="vivek", bg = "Red") 
lable1.pack(side="left",fill= "both",expand=True) 

lable2 = tk.Label(window,text="Hii", bg = "Green")
lable2.pack(side="left", fill='both', expand=True) 

lable3 = tk.Label(text="How are you", bg="Blue")
lable3.pack(side="left",fill='both',expand= True) 
'''
'''
my_frame = ttk.Frame()
my_frame.pack(side="left", fill="both",expand=True) # on left side space is created

lable1 = tk.Label(my_frame,text="vivek", bg = "Red") # lable1 is utilize the space of my_frame
lable1.pack(side="left",fill= "both",expand=True) 

lable2 = tk.Label(window,text="Hii", bg = "Green") ## if we write window or not it will not it will given to defalut by python
lable2.pack(side="left", fill='both', expand=True) 

lable3 = tk.Label(text="How are you", bg="Blue")
lable3.pack(side="left",fill='both',expand= True) 
'''
'''
my_frame = ttk.Frame()
my_frame.pack(side="left", fill="both",expand=True) # on left side space is created

lable1 = tk.Label(text="vivek", bg = "Red") 
lable1.pack(side="left",fill= "both",expand=True) 

lable2 = tk.Label(my_frame,text="Hii", bg = "Green") # lable2 is utilize the space of my_frame
lable2.pack(side="left", fill='both', expand=True) 

lable3 = tk.Label(text="How are you", bg="Blue")
lable3.pack(side="left",fill='both',expand= True) 
'''
'''
my_frame = ttk.Frame()
my_frame.pack(side="left", fill="both",expand=True) # on left side space is created

lable1 = tk.Label(my_frame,text="vivek", bg = "Red") 
lable1.pack(side="left",fill= "both",expand=True) 

lable2 = tk.Label(my_frame,text="Hii", bg = "Green") # lable1 and lable2 is utilize the space of my_frame
lable2.pack(side="left", fill='both', expand=True) 

lable3 = tk.Label(text="How are you", bg="Blue")
lable3.pack(side="left",fill='both',expand= True) 
'''



my_frame = ttk.Frame()
my_frame.pack(side="left",fill="both",expand=True)

lable1 = tk.Label(my_frame,text="vivek", bg = "Red") # lable1 is a sub frame of my_frame in this only one sub frame is here so it will utilise all the space of sub frame 
lable1.pack(side="top", fill='both',expand=True) # fill= 'both' means use all the space on x and y axis

lable2 = tk.Label(window,text="Hii", bg = "Green")
lable2.pack(side="top", fill='both', expand=True) # fill= 'both' means use all the space on x and y axis

lable3 = tk.Label(text="How are you", bg="Blue")
lable3.pack(side="top",fill='both',expand= True) # fill= 'both' means use all the space on x and y axis

window.mainloop()