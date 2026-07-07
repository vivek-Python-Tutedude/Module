'''
Inheritance:
# A mechanism that allows a new class (subclass/derived class) to acquire the
properties and behaviors (attributes and methods) of an existing class
(superclass/base class).

# Promotes code reusability and establishes an "is-a" relationship (e.g., A Car
"is a" Vehicle).

Concept: Inheritance is a mechanism where a new class (called the derived class,
subclass, or child class) inherits properties (attributes) and behaviors (methods) from
an existing class (called the base class, superclass, or parent class).
# "Is-a" Relationship: Inheritance models an "is-a" relationship. For example, a Car
"is a" Vehicle, a Dog "is an" Animal.

Benefits:
# Code Reusability: You don't have to rewrite common attributes and methods
in new classes. They are inherited from the parent.
# Extensibility: You can extend the functionality of existing classes without
modifying them.
# Maintainability: Changes in the base class are automatically reflected in all
derived classes.
'''

"""
# Syntax:

class BaseClass:
# ... attributes and methods ...
    pass
class DerivedClass(BaseClass): # DerivedClass inherits from BaseClass
# ... additional attributes and methods specific to DerivedClass ...
    pass
"""

class Vehical :
    company = "BMW Motors"

    def __init__(self, n_wheel, n_seats, mileage):
        self.n_wheel = n_wheel
        self.n_seats = n_seats
        self.mileage = mileage
        
    def get_details(self):
        return f"This vehical has {self.n_wheel} wheel, {self.n_seats} seats and provide the mileage of {self.mileage}"
    
v1 = Vehical(4, 7, 20)
print(v1.get_details())

class Car(Vehical) :
    pass

# Car class inherits the Vehical class
# Car class is called as derived / child class
# Vehical class is called as base / parent class

