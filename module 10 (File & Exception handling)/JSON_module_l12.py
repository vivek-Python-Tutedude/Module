'''
JSON == JavaScript object nptation
JSON ==> it provides utility that we need to effectively handel the JSON data


'''
import json
students = {'student1' : {'roll' : 101, 'name' : 'vivek', 'percentage' : 94.12 , "sprots" : True},
            'student2' : {'roll' : 102, 'name' : 'akash', 'percentage' : 94.60, "sprots" : True},
            'student3' : {'roll' : 103, 'name' : 'nandu', 'percentage' : 94.10, "sprots" : False}
            }
print(students)
print(type(students))

print("\n ")
# dump() ==> we can write a contents in proper json format
# syntax ==> dump(file_nm, variable (fh), indent = value)

with open("student_data_l12.json","w") as fh : # it will store the dictionary
    json.dump(students, fh)
    
with open("student_data_l12.json","w") as fh : # it will store the dictionary
    json.dump(students, fh, indent=4)
    
# load() ==> it is used for loding the data

with open("student_data_l12.json","r") as fh :
    data = json.load(fh)
    print(data, type(data))

print("\n ")
# update() ==> it is used for update the data

students = {'student1' : {'roll' : 101, 'name' : 'vivek', 'percentage' : 94.12 , "sprots" : True},
            'student2' : {'roll' : 102, 'name' : 'akash', 'percentage' : 94.60, "sprots" : False},
            'student3' : {'roll' : 103, 'name' : 'nandu', 'percentage' : 94.10, "sprots" : False}
            }

# step 1 ==> read the old data from the json file
try :
    with open("student_data_l12.1.json", 'r') as fh : # if file exists it will read data from that
        data = json.load(fh)                        # if file does not exists it go to except block and create a file store the value
        
except FileNotFoundError :
    with open("student_data_l12.1.json", 'w') as fh :
        data = json.dump(students, fh, indent=4)
    
else :   
    # step 2 ==> update operation
    data.update(students)

# step 3 ==> write the updated data into the json file

    with open("student_data_l12.1.json", 'w') as fh :
        json.dump(data, fh)

print(data)