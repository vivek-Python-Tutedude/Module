def even_odd(no) :
    if no % 2 == 0 :
        print(f"{no} is even no.")
    else :
        print(f"{no} is odd no.")
even_odd(4)
result = even_odd(7)
print(result) # in this the function is not return any thing so by defalut it return None


def even_odd(no) :
    if no % 2 == 0 :
        return f"{no} is Even."
    else :
        return f"{no} is Odd."
even_odd(4)
result = even_odd(7)
print(result) # it will return as per function it will not return None

def arithmatic(n1,n2) :
    return f"addition of {n1} and {n2}: {n1 + n2}",f"substraction of {n1} and {n2}: {n1 - n2}",f"multiplication of {n1} and {n2}: {n1 * n2}",f"divison of {n1} and {n2}: {n1 / n2}"
# we can write multiple return values as per above 

# we can't write multiple return keyword in one function like below
'''  return f"substraction of {n1} and {n2}: {n1 - n2}" 
    return f"multiplication of {n1} and {n2}: {n1 * n2}"
    return f"divison of {n1} and {n2}: {n1 / n2}"
'''

result = arithmatic(10,5)
print(result)


def arithmatic(n1, n2) :
    add = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    div = n1 / n2
    return add, sub,mul,div

n1 = int(input("Enter the no n1: "))
n2 = int(input("Enter the no n2: "))

res1, res2, res3, res4 = arithmatic(n1, n2)  # all the res variables store the value as per order of rturning of value
print(f"add = {res1}, sub = {res2}, mul = {res3}, div = {res4}")