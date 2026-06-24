import pickle
std = {'student1' : {'roll' : 101, 'name' : 'vivek', 'percentage' : 75.12 , "sprots" : True},
            'student2' : {'roll' : 102, 'name' : 'akash', 'percentage' : 94.60, "sprots" : True},
            'student3' : {'roll' : 103, 'name' : 'nandu', 'percentage' : 90.0, "sprots" : False}
            }

print(std)
print(type(std))

with open("std_l13.bin", 'bw') as fh :
    for s in std:
        pickle.dump(std[s], fh)
        
# deseseialization 

with open("std_l13.bin", 'br') as fh :
    while True :
        try:   
            data = pickle.load(fh)
            print(data)
        except EOFError:
            print("done!")
            break
        
# print the name of the students who scored 90 or more marks percent as a list
print("\n")
std_ls_90 = []
with open("std_l13.bin", 'br') as fh :
    while True :
        try:   
            data = pickle.load(fh)
            if data['percentage'] >= 90 :
               std_ls_90.append(data['name'])
        except EOFError:
            print("done!")
            break
print(std_ls_90)
