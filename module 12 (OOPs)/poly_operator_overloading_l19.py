'''
Operator Overloading
Operator overloading allows you to define how standard Python operators (like +, -, *, ==,
etc.) behave when applied to instances of your custom classes.

7.1 What is Operator Overloading?
 Concept: Giving extended meaning beyond their predefined operational meaning. For
example, the + operator usually performs addition for numbers and concatenation for
strings. With operator overloading, you can define what + means when applied to
objects of your own class.

 How it's Achieved: Python achieves operator overloading through special methods
(also known as dunder methods or magic methods) that begin and end with double
underscores (e.g., __add__, __sub__, __eq__). When you use an operator on an
object, Python internally calls the corresponding dunder method.

'''

'''
Common Operators and Their Dunder Methods
Operator Dunder Method Description
+       __add__(self, other) Addition
-       __sub__(self, other) Subtraction
*       __mul__(self, other) Multiplication
/       __truediv__(self, other) True division
//      __floordiv__(self, other) Floor division
%       __mod__(self, other) Modulo
**      __pow__(self, other) Exponentiation
==      __eq__(self, other) Equality (self == other)
!=      __ne__(self, other) Inequality (self != other)
<       __lt__(self, other) Less than (self < other)
<=      __le__(self, other) Less than or equal to (self <= other)
>       __gt__(self, other) Greater than (self > other)
>=      __ge__(self, other) Greater than or equal to (self >= other)
str()   __str__(self) String representation for users (e.g., print())
repr()  __repr__(self) Official string representation for developers
len()   __len__(self) Length of the object 19
[]      __getitem__(self, key), 
        __setitem__(self, key, value),
        __delitem__(self, key) Indexing/slicing (e.g., obj[key])

'''


# help(int)

a = 10
b = 20

# 'a' and 'b' both are objects of class int because it store the integer value

print("Addition = ",a + b) 

# __add__  and other in help(int) they some are dunder / magic method
print("Add = ",a.__add__(b)) 
print("Add2 = ",int.__add__(a,b))
# a + b == a.__add__(b) == int.__add__(a, b) all are same

s1 = "Vivek"
s2 = " Satpute"
print("Concatination = ",s1 + s2)
print("Con = ",s1.__add__(s2))
print("Con = ",str.__add__(s2, s1))
# s1 + s2 == s1.__add__(s2) == str.__add(s1, s2) all are same


class A:
    def f1(self, val):
        pass
    
    
obj = A()
obj.f1(10) # obj.f1(20)

# conclusion ==>
#   int class having the __add__() ,str also has a __add__(), and both are behave differrntly 
# depending upon how it is defined internaly

print("----------------------------------------")

class Rectangle:
    def __init__(self, len, bdth):
        self.len = len
        self.bdth = bdth
    
    def area (self) :
        return self.len * self.bdth
    
    def __add__(self, other):
        print(f"Addition of len of 2 rectangle : {self.len + other.len}")
        print(f"Addition of bdth of 2 rectangle : {self.bdth + other.bdth}")
        print(f"Addition of  2 rectangle : {self.area() + other.area()}")
        print(f"Addition of len one rectangle and bdth of another rectangle  : {self.len + other.bdth}")

r1 = Rectangle(5, 4)
r2 = Rectangle(4, 6)
print(f"Area of r1 = {r1.area()}")
print(f"Area of r2 = {r2.area()}")

# without adding the __add_()== method as per below
# print(r1 + r2) # TypeError: unsupported operand type(s) for +: 'Rectangle' and 'Rectangle'


# after adding the __add_()== method as per below
r1 + r2



