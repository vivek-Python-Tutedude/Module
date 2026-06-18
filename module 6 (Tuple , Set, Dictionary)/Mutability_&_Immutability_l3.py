# Mutability & Mutability
# Mutability => If a datatype like list is able to change the state of it's own without changing the memory address of it self it is cslled Mutability 
# List are Mutable => We can the state of the value
# Tuples & Strings are Immutable => we can't change the state of the value

# string =>  because String can not change
s1 = "vivek satpute"
s2 = s1.replace("vivek", "akash") # Return a *copy* with all occurrences of substring old replaced by ne
print(s1)
print(s2)
# s1[0] = "a" # 'str' object does not support item assignment

# Tuples

t1 = ("Mango", "Apple", "Orange")
print(t1)
print(type(t1))
# t1.append("Banana") # it gives error => 'tuple' object has no attribute 'append'  because Tuples can not change
print(t1)

# List => List cna be changed

l1 = ["Mango", "Apple", "Orange"]
print(l1)
print(id(l1)) # id() => it returns memory address
print(type(l1))
l1.append("Banana") 
print(l1)
print(id(l1)) # after modifying if memory address is not change it confirms exsiting list is modify

l2 = ["Mango", "Aple", "Orange"]
print(l2)
print(id(l2))
l2[1] = "Apple"
print(l2)
print(id(l2))
