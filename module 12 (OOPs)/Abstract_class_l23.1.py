'''
Abstraction:
o Focusing on essential features and hiding complex implementation details.

o Providing a simplified, high-level view to the user (or other parts of the
program). 

(e.g., You use a remote to change TV channels without needing to
know the complex electronics inside).

'''

from import_my import Shape
class Square(Shape) :
    def __init__(self, side):
        self.side = side
        
    def area (self) :
        return self.side ** 2

class Rectangle(Shape) :
    def __init__(self, len, bdth):
        self.len = len
        self.bdth = bdth
        
    def area(self) :
        return self.len * self.bdth
    
class Circle(Shape) :
    def __init__(self, radius):
        self.radius = radius 
    
sq1 = Square(12)
print("Area of square =",sq1.area())

r1 = Rectangle(5, 6)
print("Area of rectangle =",r1.area())

# c1 = Circle(20) # TypeError: Can't instantiate abstract class Circle without an implementation for abstract method 'area'



# Abstract class ==> in this class it containt one or more abstact method
# Abtract method ==> it is a method that has a declaration but no implementation of it's own 
# Abstact class force the all the classes to impelemnt the abstact method 
# in this above circle case we can't creat only object it gives error 