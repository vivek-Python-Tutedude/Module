'''
lambda function == the fuction  doesn't contain any name
It is also called as anonymous function
In this we can pass the argument as  well as we can pass the expression in a single line

# syntax ==> lambda arguments_nm : expression
'''
def add(a) :
    return a + 1

print(f"add = {add(5)}")

fun = lambda a : a + 1
print(fun(2))



def add(a, b) :
    return a + b

print(f"add = {add(5, 7)}")

fun1 = lambda a, b : a + b
print(f"fun1 = {fun1(110, 45)}")