class Salary_Error(Exception):
    pass

# raise Salary_Error("Invalid salary")

def check_salary(salary):
    if salary < 0 :
        raise Salary_Error("Salary cannot be negative")
    else :
        bouns = 0.1 * salary
        return salary + bouns
    
salary = int(input("enter the salary : "))
final_salary = check_salary(salary)
print(final_salary)