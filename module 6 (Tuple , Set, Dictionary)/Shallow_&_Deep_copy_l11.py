import copy
# it will be done on mutable datatypes
l1 = [1, 2.5, [10, 20, 30], 'python']

 # shallow copy ==> outer list having different address but inner list having same address
 
l2 = copy.copy(l1)
# print(l2)
# print(id(l1),"   ",id(l2))

l1[0] = 100
print(f"l1 --> {l1}, {id(l1)}")
print(f"l2 --> {l2}  {id(l2)}")

l1[2][0] = 100
print(f"l1 --> {l1}, {id(l1)}")
print(f"l2 --> {l2}  {id(l2)}")

print("\n")
# deepcopy() ==> outer list having different address AND inner list having different address
l3= [1, 2.5, [10, 20, 30], 'python']
l4 = copy.deepcopy(l3)

l3[0] = 200
print(f"l3 --> {l3}, {id(l3)}")
print(f"l4 --> {l4}  {id(l4)}")

l3[2][0] = 100
print(f"l3 --> {l3}, {id(l3)}")
print(f"l4 --> {l4}  {id(l4)}")


std1 = {'id' : 10, 'name' : 'vivek', "marks" : {'math' : 90, "eng" : 45.6, "bio" : 33}}
# deepcopy()
std2 = copy.deepcopy(std1)
std1['name'] = "akash"
print(f"std1l --> {std1}, {id(std1)}")
print(f"std2 --> {std2}  {id(std2)}")

std1['marks']['math'] = 77
print(f"std1l --> {std1}, {id(std1)}")
print(f"std2 --> {std2}  {id(std2)}")

print("\n")
# shallowcopy()
std2 = copy.copy(std1)
std1['name'] = "akash"
print(f"std1l --> {std1}, {id(std1)}")
print(f"std2 --> {std2}  {id(std2)}")

std1['marks']['math'] = 77
print(f"std1l --> {std1}, {id(std1)}")
print(f"std2 --> {std2}  {id(std2)}")