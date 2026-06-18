std1 = {"maths" : 80.5, "eng" : 76.5, 'phy' : 90}
print(std1)

# how to fetch the marks of phy
print(std1['phy'])
# print(std1["chem"]) KeyError: 'chem'

# 2nd method get() => if value is not present then it will return None
# syntax => get(key) or get(key, default_value)
print(std1.get("phy"))
print(std1.get("chem")) # it will return None
print(std1.get("chem", 700)) # it will return default value because key is not present and defalut value 700 is given
print(std1.get("phy", 50000)) # it will return orignal value because key is present

# membership operator 
# in operator => if key is present it will return True
# in operator will check the key not the value
emp1 = {'id' : 1, "name" : "vivek", "salary" : 2000000}
print('id' in emp1) # True it is the string
print(id in emp1) # False  it is an object
print(1 in emp1) # False\
    
# not in operator => if key is present it will return False
# not in operator will check the key not the value
emp1 = {'id' : 1, "name" : "vivek", "salary" : 2000000}
print('id' not in emp1) # False it is the string
print(id not in emp1) # True  it is an object
print(1 not in emp1) # True


# update() => it will update the key value pairs of another dictionary inside exsisting dictionary
sem1 = {"maths" : 80.5, "eng" : 76.5, 'phy' : 90}
sem2 = {"chem" : 85, "bio" : 87}
sem1.update(sem2)
print(sem1)

groceries1 = {'milk' : 30, 'biscuit' : 20, 'rice' : 70}
groceries2 = {'bread' : 55, 'rice' : 100}
groceries1.update(groceries2) # if value is not exsist it will add if value is exist it will update it
print(groceries1)

# pop() => it will delet the key value pair
groceries1.pop('milk')
print(groceries1)
# groceries1.pop('milk') KeyError: 'milk'

groceries1 = {'milk' : 30, 'biscuit' : 20, 'rice' : 70,'milk' : 60}
print(groceries1) # keys can not be duplicated & most recent value is atteched to the key
