class Student :
    pass

student1 = Student()
student2 = Student()

# student1 & student2 are the object of the class Student
 
student1.name = "vivek" 
student1.Rollno = 44

# We created the attribute of the student1 object

print(student1.name) # vivek
print(student1.Rollno) # 44

# print(student2.name) # AttributeError: 'Student' object has no attribute 'name'
# print(student2.Rollno) # because of runtime error it will does not run this line

print(student1.__dict__) # {'name': 'vivek', 'Rollno': 44}