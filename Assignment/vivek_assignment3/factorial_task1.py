'''
Using the user input find the factoral of the number using the recursion and loop

'''

# using loop

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact  * i # calculating the factorial
    return fact  # this function returns the fact whichn consist the actual factorial value
    
n = int(input("Enter a number : ")) # taking the user input
f = factorial(n) # calling hte factorial function with argument 'n' and store the value in f
print("Factorial Using the loop")
print(f"Factoral of {n} is: {f}") # printig the factorial 
print("============================")



# using recursion

def factorial(n):
    if n == 1:
        return 1 # when n == 1 it retruns 1 therefor factorial(1) = 1  ==> 1 * 2 * 3 * ...  * n
    else :
        fac = n * factorial(n - 1)  # calculating the factorial
    return fac # this function returns the fact whichn consist the actual factorial value
    
n = int(input("Enter a number : ")) # taking the user input
f = factorial(n) # calling hte factorial function with argument 'n' and store the value in f
print("Factorial Using the Recursion")
print(f"Factoral of {n} is: {f}") # printig the factorial 