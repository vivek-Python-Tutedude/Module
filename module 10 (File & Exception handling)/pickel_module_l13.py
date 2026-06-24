'''
serialization ==> datatypes are stored into memory for storing it will be converted into sequence of byte so computer can understand
it is called serialization
deserialization ==> when we have to access it so it will be reconverted it is called deseialization

pickel ==> it will works with binary files

'''

students = {'student1' : {'roll' : 101, 'name' : 'vivek', 'percentage' : 94.12 , "sprots" : True},
            'student2' : {'roll' : 102, 'name' : 'akash', 'percentage' : 94.60, "sprots" : True},
            'student3' : {'roll' : 103, 'name' : 'nandu', 'percentage' : 94.10, "sprots" : False}
            }
print(students)
print(type(students))
'''
with open("std_dic_l13.txt","wt") as fh :
    fh.write(students)  # TypeError: write() argument must be str, not dict'''
    
    
'''with open("std_dic_l13.txt","wt") as fh :
    fh.write(str(students))  '''
    
'''with open("std_dic_l13.txt","rt") as fh :
    for stusents in fh :
        print(students)'''
        
'''with open("std_dic_l13.txt","rt") as fh :
    content = fh.read()
    
print(type(content))
out = dict(content)
print(out)'''

import pickle

# seriallization 

std = {'student1' : {'roll' : 101, 'name' : 'vivek', 'percentage' : 94.12 , "sprots" : True},
            'student2' : {'roll' : 102, 'name' : 'akash', 'percentage' : 94.60, "sprots" : True},
            'student3' : {'roll' : 103, 'name' : 'nandu', 'percentage' : 94.10, "sprots" : False}
            }
print(std)
print(type(std))

with open("std_l13.bin", 'bw') as fh :
    for s in std:
        pickle.dump(std[s], fh)
        
# deseseialization 

with open("std_l13.bin", 'br') as fh :
    data = pickle.load(fh)
    print(type(data))
    print(data)
    
    data2 = pickle.load(fh)
    print(type(data2))    
    print(data2)

    data3 = pickle.load(fh)
    print(type(data3))
    print(data3)
    
    '''data4 = pickle.load(fh) # error ==> EOFError: Ran out of input  # this data is not exists
    print(type(data4)) 
    print(data4)'''
