'''
def add(a, c ,b = 10) :  # in this b is the default arument
    print(f"a = {a}, b ={b}, c = {c}")
    return a + b + c
result = add(10, 4, 1, 6) # it also gives error as per below because we passing the 4 argument insted of 3
# TypeError: add() takes from 2 to 3 positional arguments but 4 were given
print(result)

'''
# variable length argument :- with the help of that we can pass "n" no of argument 
# *args = *(n) no of argument(args) we can change the variable name args(it is an only variable name)
# args = datatype of args is tuple
# the functionality of star(*) is to take multiple value (we can give "n" no of args )
# args will store all these values as a tuple
 
def add(*args) :
    print(f" args = {args},datatype ={type(args)}")
    print(f"sum = {sum(args)}")
    
add(10, 16, 13)
add()

def stu_detail(sid, sname, *marks) :
    if len(marks) == 0 :
         print(f"{sname} with id {sid} secured 0 %")
    else :
        precentage = sum(marks) / len(marks)
        print(f"{sname} with id {sid} secured {precentage}%")

stu_detail(1, "vivek", 87, 95 , 96, 87, 88)
stu_detail(2, "akash", 87, 95 , 96, )
stu_detail(3, "rohit")