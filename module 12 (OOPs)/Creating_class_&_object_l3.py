''' 
Creating a class
syntax ==> class Class_Name :
                attributes and function

'''
class My_Class : # empty class
    pass

# Creating a object
obj1 = My_Class()
obj2 = My_Class()
# obj1 & obj2 are object of My_Class

print(type(obj1)) # <class '__main__.My_Class'> # __main__ occure because both are in same module
print(type(obj2)) # <class '__main__.My_Class'>

# methods ==> any function defined inside the class it is called as method

# calling method using the method

class Student :
    """
    This is a class student to manage student info and activities
    """
    pass

s1 = Student()
s2 = Student()

# Doc strings ==> documemtation or details about the class __doc__ or using the help()

print(Student.__doc__) # This is a class student to manage student info and activities

print(help(Student))
'''

Help on class Student in module __main__:                                                            

class Student(builtins.object)
 |  This is a class student to manage student info and activities
 |
-- More  -- 

'''
