# concatination
sd1 = (1001, "vivek")
sd2 = (78.5, 91.0,83, 79.5)
sd = sd1 + sd2
print(sd)

# Repetation
t1 = ("class 5", 5000)
print(t1 * 3)

# Membership 
# in => it check item is part of the Tuple if yes True else False

print(sd)
print("vivek" in sd)
print("class 5" in sd)
 
# not in => it check item is part of the Tuple  if no True else False

print(sd)
print("vivek" not in sd)
print("class 5" not in sd)

# some read operations

# count() => Return number of occurrences of value.
# synatx = tuple_nm.count(element) # (elemtent not a index)

t1 = (10, 3, 4, 6, 0,-1, 10, 3, 10, 3)
print(t1.count(10))

# index() => Return *first* index of value.
# synatx = tuple_nm.index(element) 
print(t1.index(-1))
print(t1.index(10)) #  Return *first* index of value.
# print(t1.index(40)) #  tuple.index(x): x not in tuple

# min(Tuple_nm) => return its smallest item.
# max(Tuple_nm) => return its biggest item.
# sum(Tuple_nm) => it returns the sum

t1 = (10, 3, 4, 6, 0,-1, 10, 3, 10, 3)
print(min(t1))
print(max(t1))
print(sum(t1))
