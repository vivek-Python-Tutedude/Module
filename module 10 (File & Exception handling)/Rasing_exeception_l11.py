# Raise :- we can create custom exception as per our condition

salary  = float(input("Enter the salary"))

if salary < 0:
    raise ValueError("Salary cannot be negative")
else :
    print(f"Your salary is {salary}")
    
    
age  = float(input("Enter the age"))

if age < 0:
    raise Exception("age cannot be negative") # Exception ==> all the errors under exception (Generic exception)
else :                                      # all the run time errors are comes under this exception error
    if age >= 18:
        print("You can vote")
    else :
        print("You cannot vote")
