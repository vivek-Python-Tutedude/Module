# Tuples= => it is the comma seperated element enclose in paranthesis.
# Tuple_name =(item1, item2, ......)
# it is the sequence of item as a collection
# it will also story any data types like list
# in tuples element are fixed
# like in list we can insert, extend, append for add element to the list but in tuple we can't do this.
# like in list we can pop and remove for delete the element but in tuple we can't do this
# # like in list we can reverse() for revesr thr list
# # sort() for sort the list we can't do this in tuples
# because   in tuples element are fixed
# we can't modify or extend the tuples


T1 = ("python", 10, 5.5, True, None, [1, 2, 3, 4], (5, 6, 7))
print(T1)
print(type(T1))
print(len(T1))

print("\n")
# Accessing item of a Tuple  -  index # it support indexing

print(T1[0])
print(T1[-1])
print(f"Accessing element 7 in Tuple inside Tuple: {T1[-1][2]}")

# slicing in Tuples
t2 = ("python", 10, 5.5, True, None, [1, 2, 3, 4], (5, 6, 7))
print(type(t2))
print(t2[0 : 4 : 1])
print(t2[ :  : ])

print("\n")

# 2nd method of defineing the tuple
t1 = 10, 20, 30
print(type(t1))

# the sequence item as a collection, comma seperated elements enclose within paranthesis and inthis paranthesis is optional
# tuples can created without the paranthesis
print("\n")
# converting list into tuples (Typecasting)
l1 = [1, 2, 3, 4]
print(l1)
print(type(l1))
t3 = tuple(l1)
print(t3)
print(type(t3))

#  converting tuple into list

fruits = ("Mango", "Apple","Orange")
print(fruits)
print(type(fruits))
fruits = list(fruits) # re assign to the same variable
print(fruits)
print(type(fruits))