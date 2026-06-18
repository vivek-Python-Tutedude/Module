# Dictionary = it is the comma seperated key - value pairs enclosed within curly brackets {}.
# Each key-value pair is seperated by colon (:) = {key1 : value1, key2 : value2, ....}
# 
groceries = {"milk" : 30, "biscuits" : 10, 'rice':70, """bread""" : 20}
print(type(groceries))
print(groceries)

groceries1 = {'milk' : 30, 'biscuit' : 20, 'rice' : 70,'milk' : 60}
print(groceries1) # keys can not be duplicated & most recent value is atteched to the key

# len() => it gives the num of pairs present in dictionory
print(len(groceries))

# it does ont have indexing but we can access the element using key
# print(groceries[0])

print(groceries["milk"])
# print(groceries["eggs"]) KeyError: 'eggs'

# dictionary are mutable we can change the value
print(groceries)
groceries["biscuits"] = 20
print(groceries)

# adding the value in dictionary
groceries["eggs"] = 11
print(groceries)


groceries["biscuits"] = 35
print(groceries)
# *** if key is present it will update the value ***
# *** if key is not present it will add that value ***
