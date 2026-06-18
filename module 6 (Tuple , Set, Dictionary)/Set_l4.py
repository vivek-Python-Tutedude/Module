# sets are collection of items
# set are non squential collection of item
# it is created by writting comma seperated elements or items enclosed within curly brackets {}
# it can store multiple data types

s1 = {10, "vivek", 2.5}
print(type(s1))
print(s1)

# length of set
print(len(s1))


# it does mot supports indexing
# print(s1[0]) #  'set' object is not subscriptable

# it does mot supports slicing
# print(s1[1 : 5 : 1]) # 'set' object is not subscriptable

# ### Sets are data structures which do not have duplicates element in them
# each elemnt in set are must be uniqe

# list
s2 = [10, 2.5, 10, 2.5, 3, 10]
print(type(s2))
print(s2)

# sets => each elemnt in set are must be uniqe
s3 = {10, 2.5, 10, 2.5, 3, 10} # It will does not givs error it will discard the duplicate element
print(type(s3))
print(s3)


