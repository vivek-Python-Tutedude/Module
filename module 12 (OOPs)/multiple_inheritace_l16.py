'''
Multiple Inheritance
Definition: A class inherits from more than one base class. The derived class gets
attributes and methods from all its parent classes.
 Diagram:
 Class A   Class B
 ^            ^
 |            |
 +------+------+
        |
        v
     Class C
 Example: Flyer + Swimmer -> Duck

'''
class A :
    def state_1(self):
        print("State_1 present")
    def state_2(self):
        print("State_2 present")
    def state_3(self):
        print("State_3 present")

class B :
    
    def state_4(self):
        print("State_4 present")
    def state_5(self):
        print("State_5 present")
        
class C(A, B) :
    def state_6(self):
        print("State_6 present")
    
a = A()
a.state_1(), a.state_2(), a.state_3()
# obj a has only 3 (1, 2, 3) state access

print("----------------------\n")

b = B()
b.state_4(), b.state_5()
# obj b has only 2 (4, 5) state access

print("----------------------\n")

c = C()
c.state_1(), c.state_2(), c.state_3(), c.state_4(), c.state_5(), c.state_6()
# obj c has all 6 (1, 2, 3, 4, 5, 6) state access

print("----------------------\n")


class Flyer:

    def fly(self):
        print("I can fly!")
        
class Swimmer:
        def swim(self):
            print("I can swim!")
         
class Duck(Flyer, Swimmer): # Duck inherits from both Flyer and Swimmer
    def quack(self):
        print("Quack! Quack!")
     
     
my_duck = Duck()
my_duck.fly()
my_duck.swim()
my_duck.quack()