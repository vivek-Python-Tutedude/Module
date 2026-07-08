

class A :
    def add(self, n1, n2) :
        return n1 + n2
    
    def add(self, n1, n2, n3) :
        return n1 + n2 + n3
    
obj = A()
print("Addition of 3 no = ",obj.add(1, 2, 3))

# print("Addition of 2 no = ",obj.add(1, 2)) # TypeError: A.add() missing 1 required positional argument: 'n3'
# above statement gives error because python does bo support method overloading
# it will override the method with latest one like here it will overide with additon of 3 no