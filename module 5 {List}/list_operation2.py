# extend() => in this we can add multiple item into the end of the list
# it will add element one by one not as a single element
fruits = ["Mango", "Apple", "Orange"]
l1 = [1, 2]
# fruits.append("Grapes", "Banana")  we can't give multiple input

fruits.extend(["Grapes", "Banana"])
print(fruits)
fruits.extend(l1)
print(fruits)
# fruits.extend("vivek","akash") it should be in the form of list


# remove() => it is used to remove only one item at a time

fruits.remove("Banana")
print(fruits)

# fruits.remove("Banana") # x not in list  value does not exist error 

fruits.insert(3, "Apple")
print(fruits)
fruits.remove("Apple") # it will remove first occurence
print(f"it will remove first occurence: {fruits}")

print("\n")


# pop() => with the help of index it will delete the item

fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

# fruits.pop(110) # pop index out of range error
fruits.pop() # if we don't give the value to pop() then last item will delete
print(fruits)