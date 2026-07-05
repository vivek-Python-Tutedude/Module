'''
Class variables are defined at the class level.
same copy of the class variable are shared amomg the object

'''


class Student :
    """
    This is a class student to manage student info and activities
    
    """
    clg_nm = "DKTE"
    dept = ["Arts", "commerce", "Science"]
    
    def __init__(self, name, rollno):
        self.name = name   # obj_nm.attribute_nm = value --> syntax
        self.rollno = rollno # self variable consist the calling object

s1 = Student("vivek", 1)
print(s1.__dict__) # we cannot print class variables like this
print(Student.clg_nm) # we can access using the class name
print(s1.dept) # also we can access using the object name

s2 = Student("Akash", 2)
s2.Grade = "A"
print(s2.__dict__, s2.clg_nm, Student.dept)