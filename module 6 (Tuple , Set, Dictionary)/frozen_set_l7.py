# normal sets are Mutable set
s1 = {1, 3, 5, 0}
s1.add(-1)
print(s1)

# frozen set are Immutable set
# it is used to store the non duplicate or unique elemnt but it is immutable we cna't change the set
fs1 =  frozenset({10, 5, 9,})
print(fs1, type(fs1))

# fs1.add(40) # AttributeError: 'frozenset' object has no attribute 'add'

fs2 =frozenset({19, 10, 3, 5})
print(fs2)
print(fs1 & fs2) #  --> intersection
print(fs1 | fs2) #  --> union
print(fs1 - fs2) # element of fs1 which not a part of fs2
print(fs2 - fs1) # element of fs2 which not a part of fs1
print(fs1 - fs1) # empty frozenset()