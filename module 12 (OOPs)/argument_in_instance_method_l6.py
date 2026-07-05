class Student :
    """
    This is a class student to manage student info and activities
    
    """
    def study(self, n_hrs):  # we can pass multiple arguments
        print(f"Self is : {self}")     
        print(f"The student is studies for {n_hrs} Hr a day!")
    
    def sports(self, sports_name) : # we can create N no of instance method in one class
        print(f"Self is : {self}")     
        print(f"The student plays {sports_name}")
        
        
student1 = Student()
print(f"student1 = {student1}") 
student1.study(3)  # we can pass multiple arguments (here 2 args are pass 1st is self 2nd is n_hrs == 3)
student1.sports("Football") # obj_nm.attribute_nm = value --> syntax

print("------------------------")

student2 = Student()
print(f"student2 = {student2}") 
student2.study(4) 
student2.sports("Cricket")
