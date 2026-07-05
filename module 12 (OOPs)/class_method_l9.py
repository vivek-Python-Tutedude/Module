'''
Class method are method defined inside the class that are bound to the class not to the instnce variable 
To create a class method we use a decorator --> @classmethod

'''

class Welcome :
    @classmethod
    def greet(self) : # in self the class is present
        print(self) # <class '__main__.Welcome'>
        print("Welcome")
        
obj = Welcome()
obj.greet() # we can call using the object name
Welcome.greet() # we can also call using the class name
print(Welcome) # printing the class welcome --> # <class '__main__.Welcome'>

print("-----------------------------------------")

class Student :
    """
    This is a class student to manage student info and activities
    
    """
    clg_nm = "DKTE"
    dept = ["Arts", "commerce", "Science"]
    
    def __init__(self, name, rollno):
        self.name = name   # obj_nm.attribute_nm = value --> syntax
        self.rollno = rollno # self variable consist the calling object

    def study(self, n_hrs):  # we can pass multiple arguments
            print(f"The student is studies for {n_hrs} Hr a day!")
    
    def sports(self, sports_name) : # we can create N no of instance method in one class
            print(f"The student plays {sports_name} for the {self.clg_nm} college")
            
    @classmethod
    def greet(cls) : # we can use any variable insed of cls but as per convention we write the cls
        print(cls) # <class '__main__.Student'>
        print(f"Welcome to {cls.clg_nm}")
        
    @classmethod
    def get_dept(cls) :
        print(f"Department in {cls.clg_nm} are: ")
        for dept in cls.dept: # we cannot do dept it gives error insted of that we hve to do cls.dept                  
            print(dept)

s1 = Student("vivek", 1)
s1.greet() # the output of greet method is as below
# <class '__main__.Student'>
# Welcome to DKTE

print(s1.__dict__) # {'name': 'vivek', 'rollno': 1}

s1.sports("cricket")
s1.get_dept()