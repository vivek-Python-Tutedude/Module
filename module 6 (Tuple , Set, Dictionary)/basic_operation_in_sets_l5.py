# Membership operator
num = {1, 3, -2, 5, 8}

# in = it is used for checking the elmemnt if exist True else False

print(1 in num)
print(2 in num)

# not in = it is used for checking the elmemnt if exist False else True

print(1 not in num)
print(2 not in num)

# we can't do indexing and slicing of sets

# concatination => it does not supports concatination
num2 = {10, 3, 56}
# print(num + num2) # unsupported operand type(s) for +: 'set' and 'set'

# repeting sets => it does not supports repetaion
# print(num * 3) # unsupported operand type(s) for *: 'set' and 'int'

# typecasting
days =("Mon", "Tue", "Wen", "Thu", "Fri", "sat", "Sun" )
print(days)
print(type(days)) # tuples --> Set & assening to diff variable we can also do viceversa
s = set(days)
print(s)
print(type(s))

days =["Mon", "Tue", "Wen", "Thu", "Fri", "sat", "Sun" ]
print(days)
print(type(days)) # list --> Set & assening to same variable we can also do viceversa
days = set(days)
print(days)
print(type(days))

print("\n")

# sets Are Mutable
 
# add() =>it will add item at randomly

s1 = {2, 0, -1, 8}
s3 = {2, 0, -1, "vivek", 8}
print(s1.add(5)) # we can't print like that it retun None bu aad operation will be performed
s1.add(5)
print(s1) 
s3.add(111)
print(s3) # it is non orderd it will print randomly
s3.add("vivek") # if element is present and we add the elemnt again it does not gives error set reamins same
print(s3)

# remove() => it will remove item

s1 = {2, 0, -1, 8}
s3 = {2, 0, -1, "vivek", 8}
print(s1.remove(0)) # we can't print like that it retun None but remove opration will be performed
s1.remove(-1)
print(s1)
# s3.remove("akash") # keyerror : elemrnt is not present

# discard() => 

s1 = {2, 0, -1, 8}
s3 = {2, 0, -1, "vivek", 8}
print(s1.discard(0)) ## we can't print like that it retun None but discard opration will not be performed
s1.discard(0)
print(s1)
s1.discard(-1)
print(s1)
s3.discard("akash") # if element is not present it will does not gives error like remove()
print(s3)