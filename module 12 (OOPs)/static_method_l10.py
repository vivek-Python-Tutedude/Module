'''
Static method ==> It is defined inside the class which is neither bound to the object nor to the class 
To create a static method we use decorator --> @staticmethod

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

    def study(self, n_hrs):  # we can pass multiple arguments
            print(f"The student is studies for {n_hrs} Hr a day!")
    
    def sports(self, sports_name) : # we can create N no of instance method in one class
            print(f"The student plays {sports_name} for the {self.clg_nm} college")
            
    @staticmethod
    def greet() : # It does not consist any default argument
        print(f"Welcome to college")
    
    @staticmethod
    def greet2(variable) : # It does not consist any default argument but progrmmer can pass the argument
        print(f"Welcome to {variable.clg_nm} college")
        
    @classmethod
    def get_dept(cls) :
        print(f"Department in {cls.clg_nm} are: ")
        for dept in cls.dept: # we cannot do dept it gives error insted of that we hve to do cls.dept                  
            print(dept)

s1 = Student("vivek", 1)

# calling the static method greet
s1.greet() # Welcome to college
Student.greet() # Welcome to college # we can call static method using the obj_nm or cls_nm

print(s1.__dict__) # {'name': 'vivek', 'rollno': 1}

print("-----------------------")

# we can pass the arguments in static method and we can pass argument like obj or class
s2 = Student("akash", 2)
print(s2.__dict__) # {'name': 'akash', 'rollno': 2}

s2.greet2(Student) # Welcome to DKTE college
s2.greet2(s2) # Welcome to DKTE college

print("-----------------------")

s1.sports("cricket")
s1.get_dept()