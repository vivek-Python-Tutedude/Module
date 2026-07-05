'''
Instance method 
   It is defined insidenthe class which is (bound to / associated with) the (instance / object)
'''

class Student :
    """
    This is a class student to manage student info and activities
    
    """
    def study(self): # insted of self we can give any valid variable name but by convention we use self
        print(f"Self is : {self}")     
        print("The student is studies for 3 Hr a day!")
        
''' 
def studyE():
        print("The student is studies for 3 Hr a day!")
''' 
     
student1 = Student()
print(f"student1 = {student1}")

# student1.studyE() #TypeError: Student.study() takes 0 positional arguments but 1 was given

student1.study() # in this python will automatically pass object student1 to study() --> it is the method

'''
When we call an instances method using the (object / instance) of a class, Python passes the object it self
as the first argument to that method

'''
print("--------------------------")

student2 = Student()
print(f"student2 = {student2}") 
student2.study() 

'''
every time if we call the instance method by the using different object so firstly that 
object itself is being passed to the method so it will understand which object is 
associated with and which object is calling

'''

