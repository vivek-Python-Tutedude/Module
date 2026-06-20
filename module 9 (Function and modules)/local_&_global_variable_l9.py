'''
local variable ==> Is nothing but we can access this variable inside the function we cannot access this variables outside the function
global variable ==>  Is nothing but we can access this variable inside the function as well as outside the function
most prefernce is given to the local variable insted of local variable
(local > global)
'''
n = 1 # globale variable
n1 = 10
v = 4
def fn() :
    n = 5 # this 'n' is local varable we can't access outside the function
    print("in",n) # printing the value of local variable ==> 5
    print("out",n1) # n1 is a globle variable
    global v
    v = 3 # changes are made in global variable because of we declare as global with global keyword
    print("in",v)

fn()
print("out",n) # both 'n' variables are different
print("out",v) # both 'v' variables are same because of we declare as global with global keyword
