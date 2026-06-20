# in python we can pass function as argumentof another function
# also we can pass multiple function as argument

def add(n) :
    return n +1
def squer(n) :
    return n ** 2

n = int(input("Enter the no: "))
res_1 = add(n)
res_2 = squer(res_1)
print("output is = ",res_2 )

res = squer(add(n)) # passing the function as a argument
print("output is = ",res )

print("new progam")

def add(n) :
    return n +1

def squer(n) :
    return n ** 2

def sub(n1 ,n2):
    return n1 - n2

n = int(input("Enter the no: "))
res_1 = add(n)
res_2 = squer(res_1)
res_3 = sub(res_2, res_1)
print("output is = ",res_2 )

res = squer(add(n)) # passing the one function as a argument
print("output is = ",res )

res = sub(squer(add(n)), add(n)) #  we can pass multiple function as argument
print("output is = ",res )
