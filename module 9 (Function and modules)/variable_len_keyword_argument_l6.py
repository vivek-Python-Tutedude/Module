# variable length keyword argument :- with the help of that we can pass "n" no of keyword argument 
# **kwargs = *(n) no of keyword argument(kwargs) we can change the variable name kwargs(it is an only variable name)
# args = datatype of kwargs is dictionary
# the functionality of star(**) is to take multiple keyword arguments  (we can give "n" no of kwargs )
# kwargs will store all these values as a key value pair as a dictionary

def pri(**kwargs) :
    print(kwargs)
pri(x = 5, y = 3)


def stu_detail(sid, sname, *extra, **marks) : # the keyword argument (**marks) it should be at last argument in function defination
    if len(marks) == 0 :
         print(f"{sname} with id {sid} secured 0 %")
         print(f"extra = {extra}")

    else :
        precentage = sum(marks.values()) / len(marks)
        print(f"{sname} with id {sid} secured {precentage}%")
        print(f"extra = {extra}")

stu_detail(1, "vivek", "cricket , football", phy = 87, che = 95 , maths = 96, bio = 87, IT =88)
stu_detail(2, "akash", "cricket , football", phy = 87, che = 95 , maths = 96, )
stu_detail(3, "rohit", "cricket , football")