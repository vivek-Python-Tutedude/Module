# reverse() => it is used to reverse the list

days_of_week = ["Mon", "Tue", "Wen", "Thur", "Fri", "Sat", "Sun"]
print(days_of_week)
days_of_week.reverse()
print(days_of_week)

print("\n")

num = [1, 5, 9, 8, 0]
print(num)
num.reverse()
print(num)

print("\n")

# sort() => it is used for sorting by default it sort into Ascending Order

num = [1, 5, 9, 8, 0]
print(num)
num.sort()
print(f"By Default sorted Ascending Order: {num}")

num = [1, 5, 9, 8, 0]
print(num)
num.sort(reverse = True)
print(f"Sorted in Descending Order: {num}")

print("\n")

# count() => it is used to count the perticular element in list 

num = [1, 5, 9, 8, 0, 1, 0, 4, 1, 1]
print(num.count(1))
'''
print(f"the list is: {num}")
item_to_count = int(input("enter the no from list: "))
c = num.count(item_to_count)
print(f"Occrrence of {item_to_count} is {c}")

lan = ["C", "C++","Python","Java","C", "C++","Python","Java"]
print(f"the list is: {lan}")
item_to_count = input("enter the String from list: ")
c = lan.count(item_to_count)
print(f"Occrrence of {item_to_count} is {c}")'''

print("\n")

# Membership operator

# in => it is used to check item is present in list or not if present it returns True or returns False

lan = ["C", "C++","Python","Java","C", "C++","Python","Java"]
print("Python" in lan)
print("Javascript" in lan)

# not in => it is used to check item is present in list or not if present it returns False or returns True


lan = ["C", "C++","Python","Java","C", "C++","Python","Java"]
print("Python" not in lan)
print("Javascript" not in lan)