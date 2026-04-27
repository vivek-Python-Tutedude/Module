# slicing of lists

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l1[1 : 4 : 1])
print(l1[1 : 7 : 3])
print(l1[0 : 15 : 2])
print("\n")
# concatenation of lists

l2 = [1, 2, 3, 4, 5]
l3 = [6, 7, 8, 9, 0]
print(l2 + l3)
print(l3 + l2)
print(l3 + l3)
print(l2 + ["vivek", 4, 11, 2.005])

# Repetation of List

print(l2 * 3)

print([1, 4, 5, 6] * 3)

# append() => it is use to add the item to the end of the list
# the item would be any data type
# syntx => list_nm.append(item)

print("\n")

fruits = ["Mango", "Apple", "Orange"]
print(fruits)
fruits.append("Banana")
print(fruits.append("Banana")) # append will add the item into the existing list
# list are mutable
print(fruits)

# insert => we can insert the item in any valid index
# syntax => list_nm.insert(index, item)


fruits.insert(0, "Banana")
print(fruits)