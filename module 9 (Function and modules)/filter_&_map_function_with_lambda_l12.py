'''
filter = It takes a function as a argument and a sequence and a second argument
It is will ues to filtering out all the elements for particular sequence for which function return true

syntax ==> filter(function, sequence)
we can't directly print filter object 
for printing output we have to convert it into the list or use for loop

'''

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
odd = lambda x : True if x % 2 != 0 else False
fun = filter(odd, seq)
print(fun) # in this we get filter object
print(list(fun))

# for even 
even = filter(lambda x : True if x % 2 == 0 else False, seq) # we can directly pass the function
print("even = ",list(even))

'''
map = It takes a function as a argument and a sequence and a second argument
It will store the what ever output we get

syntax ==> map(function, sequence)
we can't directly print map object 
for printing output we have to convert it into the list or use for loop

It is useful when we have a sequence and we want to do certain operationon each element on the sequence
'''
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
map_op = map(lambda x : True if x % 2 != 0 else False, seq) # we can directly pass the function
print(map_op) # in this we get filter object
print(f"map output =  {list(map_op)}") 

sqr = map(lambda x : x ** 2, seq)
print(f"sqr = {list(sqr)}")