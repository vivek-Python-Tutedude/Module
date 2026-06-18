#  d1 = {[1, 3, 5] : 9, [1, 2, 1] : 4}
# print(d1) TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
# keys can not be list

d1 = {"Nine" : 9, "Four" : 4}
print(d1)
d1 = {1 : 9, 2 : 4}
print(d1)
d1 = {1.2 : [9, 2 ,1], 2.1 : 40.1}
print(d1)
d1 = {True : 220, False : 1}
print(d1)
d1 = {(1, 3, 5) : 9, (1, 2, 1) : 4}
print(d1)
# d1 = {[1, 3, 5] : 9, [1, 2, 1] : 4} TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
# print(d1)
# d1 = {{1 : 9, 2 : 4} : 1} # TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
# print(d1)
# d1 = {{1, 3, 5} : 9, {1, 2, 1} : 4}
# print(d1) TypeError: cannot use 'set' as a dict key (unhashable type: 'set')

# alloed Keys => Strings, Integer, Boolean, Tuples  ==> all are mutable datatypes
# Not alloed Keys => List, Dictionary, Set  ==> immutable datatypes
# keys of a dictionary can only be mutable datatypes
# values can be any data types

std1 = {'id' : 10, 'name' : 'vivek', "marks" : [90, 45.6, 33]}
print(std1)
print(std1['marks'][1])

std1 = {'id' : 10, 'name' : 'vivek', "marks" : {'math' : 90, "eng" : 45.6, "bio" : 33}}
print(std1)
print(std1['marks']['eng'])

# fetch only the all keys == keys()
std1 = {'id' : 10, 'name' : 'vivek', "marks" : {'math' : 90, "eng" : 45.6, "bio" : 33}}
print(std1.keys(), type(std1.keys()))

# fetch only the all values == values()
std1 = {'id' : 10, 'name' : 'vivek', "marks" : {'math' : 90, "eng" : 45.6, "bio" : 33}}
print(std1.values(), type(std1.values()))

# items() ==> it gives key value pair in the form of tuple
std1 = {'id' : 10, 'name' : 'vivek', "marks" : {'math' : 90, "eng" : 45.6, "bio" : 33}}
print(std1.items(), type(std1.items()))