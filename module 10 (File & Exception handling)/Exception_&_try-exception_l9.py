'''
2 types of  error

1] compile time error ==> syntax error & indentation error
2]Excption (Run time error) ==> errors during execution 

python has built in exeption
ex:-  name error, value error, index error, key error

'''
age = 26
print(age)

# if age >= 18:
# print("You are an adult") # IndentationError: expected an indented block after 'if' statement on line 9
# above is compile time error


# print(10 / 0) # ZeroDivisionError: division by zero
# above is Exception

'''
For handling the exption we use the try - accept block

'''
'''
n1 = int(input("Enter the no 1: "))
n2 = int(input("Enter the no 2: "))

r = n1 / n2 # if n2 = 0 it gives error ==> ZeroDivisionError: division by zero
print(r)

'''
'''
n1 = int(input("Enter the no 1: "))
n2 = int(input("Enter the no 2: "))
try :
    r = n1 / n2 
    print(r)
except :
    print("The denominator cannot be zero")



n1 = int(input("Enter the no 1: "))
n2 = int(input("Enter the no 2: "))
try :
    r = n1 / n2 
    print(r)
except ZeroDivisionError:
    print("The denominator cannot be zero")

'''

try :
    n1 = int(input("Enter the no 1: "))
    n2 = int(input("Enter the no 2: "))
    r = n1 / n2 
    print(r)
except ZeroDivisionError:
    print("The denominator cannot be zero")
except ValueError :
    print("Enter only digit")