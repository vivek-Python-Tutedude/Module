'''  
for loop :-
It is an iterator based loop which step through the item of a collection (lists, tuple, sets, dict, str)
and executes a block of code repeatedly for a num of items/elements of that collection

syntax:- 
for variable_name in sequence :
    statement 1
    statement 2
    ...
    statement N
other statement

'''

per = [8.5 ,7.9 ,8 ,9.1, 5]

'''
print(per[0])
print(per[1])
print(per[2])
print(per[3])
print(per[4])
'''

for p in per :  # it run based on the length of the collection/sequence
    print(p)    # like here it will runs 4 times
