s1 = "vivek satpute"

for c in s1:
    print(c)
print("End of the loop")

employee = {'empid' : 1, 'name' : 'vivek', 'dept' : 'ENTC' }

for d in employee :
    print(d)   # if we run for loop directly on dictionary then we will get Key 
    print(employee[d]) # by using the key we can print the value
    print(d,employee[d])

print(employee.items())
# employee.item() it will give dic in the form of tuple 
for d in employee.items():
    print(d[0],d[1])
    