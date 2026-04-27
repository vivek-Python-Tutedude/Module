name = "vivek"
age = 21
lan = "python"
hr = 2

# vivek is 21 year old. He studies python 2 hours a day.

# 1st way

print(name,"is",age,"year old. He studies",lan,hr,"hours a day")

# 2nd => Formattin string

print(f"{name} is {age} year old. He studies {lan} {hr} hours a day.") 


sub1 = 85
sub2 = 81
sub3 = 88

percent = (sub1 + sub2 + sub3) / 3

print(f"{name} scored {sub1 + sub2 + sub3} marks in total")

print(f"{name} got {round(percent,2)}%")       


# Hello, vivek satpute! Welcome to the python program")
# only entering name and only last name we can not get ! like in ouput in this by normal method so here compalsary we want to use formatting string

fn = input("Enter your first name: ")
ln = input("Enter your last name: ")

print(f"Hello,{fn} {ln}! Welcome to the python program")