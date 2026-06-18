'''
range() -> build in function used to generate sequence integers
range(start, stop, step) # stop is not included

for variable_nm in range(start, stop, step) :
    statements
    
for variable_nm in range(start, stop) : # => default value of step is 1
    statements
    
for var_nm in range(stop): # defalut value of start is 0    it generate 0 - (stop - 1)
    statements

'''

for i in range(1, 11, 1): # 1, 2, 3, ....., 10
    print(i)

# generate odd no between 1 - 10
for i in range(1, 11, 2):
    print(i)
    
# generate even no between 1 - 10
for i in range(2, 11, 2):
    print(i)
    
# reverse order 10 - 1  / countdown
for i in range(10, 0, -1):
    print(i)
print("Happy new Year !!!")

# reverse order 20 - 10 only even 
for i in range(20, 9, -2):
    print(i)

for d in range(1, 5): # step by default 1
    print(d)
    
for d in range(6):  # defalut value of start is 0    it generate 0, 1, 2, 3, 4, 5
    print(d)

groceries = ["salt", "milk", "suger"]
for g in groceries :
    print(g)

for g in range(len(groceries)) :
    print(g)
    
profit = [9, 11, 6, 10]
for index in range(len(profit)):
    print(f"profit of qurter {index + 1} is {profit[index]} ")