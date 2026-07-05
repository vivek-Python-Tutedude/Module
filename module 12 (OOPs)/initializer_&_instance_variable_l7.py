'''
initializer / __init() method
it is the instance method
It is used to create and intitalize the attributres and variable during the creatiaon of the object

'''
class Student :
    """
    This is a class student to manage student info and activities
    
    """
    
    def __init__(self, name, rollno, dept):
       #      print(f"calling the init method automatically by python{self}")
        self.name = name   # obj_nm.attribute_nm = value --> syntax
        self.rollno = rollno # self variable consist the calling object
        self.dept = dept # s1.dept = "ENTC" / s2.dept = "CSE"
     
# s1 = Student() # calling the init method automatically by python<__main__.Student object at 0x000001A2EE514980>
# s2 = Student() # calling the init method automatically by python<__main__.Student object at 0x000001A2EE504550>

s1 = Student("vivek", 1, "ENTC")
# we can print the attribute values using  2 method
print(s1.name, s1.rollno, s1.dept)
print(s1.__dict__)

s2 = Student("akash", 2, "CSE")
print(s2.__dict__)

'''
Instance (variable / attribute) are different for the different objects

'''
s3 = Student("Rohit", 3, "ENTC")
s3.grade = "A" # we can add attributes outside the class also

print(s3.__dict__)