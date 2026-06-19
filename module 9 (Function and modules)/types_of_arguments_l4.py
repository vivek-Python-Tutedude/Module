def add(a, b) :
    print(f"a = {a}, b ={b}")
    return a + b

# positional argument :- passing the arguments in the order of their position
result = add(10, 5)
print(result)

# Default arrgument :- during function defination pass the argument
# In this no need the pass the value of default argument

def add(a, b = 10) :  # in this b is the default arument
    print(f"a = {a}, b ={b}")
    return a + b

result = add(10) # no need to pass the value of b because it have default value b = 10
print(result)

result = add(10, 5) # if also pass the default value in that case default value is change to b = 5 
# result = add() # if do not pass the value of 'a' it gives error as per below
# TypeError: add() missing 1 required positional argument: 'a'

'''
def add(a, b = 10, c) :  # in this b is the default arument
    print(f"a = {a}, b ={b}, c = {c}")
    return a + b + c

# result = add(10, 20, 30) # it gives error as per below because non default argument(a,c) are 
# should not follow the default argument (b) {it means we have to c argument before b} like 
# add(a, c, b ):  or   add(c, a, b) # "b" should be at last
# SyntaxError: parameter without a default follows parameter with a default

'''

def add(a, c ,b = 10,) :  # in this b is the default arument
    print(f"a = {a}, b ={b}, c = {c}")
    return a + b + c
result = add(10, 4)
print(result)


# keyword argument :- in this we use the argument name while calling the function 
def add(a, c ,b = 10,) :  # in this b is the default arument
    print(f"a = {a}, b ={b}, c = {c}")
    return a + b + c

result = add(10, c = 5) # in this 'a', 'c' is the keyword argument
print(result)


def add(a, c ,b = 10,) :  # in this b is the default arument
    print(f"a = {a}, b ={b}, c = {c}")
    return a + b + c
result = add(10, int((input("enter the value of C :"))))
print(result)