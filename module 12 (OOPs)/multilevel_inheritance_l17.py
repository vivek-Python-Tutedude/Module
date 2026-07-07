'''
Multi-Level Inheritance
Definition: A class inherits from a derived class, forming a chain. Class C inherits
from Class B, and Class B inherits from Class A (A -> B -> C).
Relationship: Grandparent -> Parent -> Child.
 Diagram:
 Grandparent Class (A)
        ^
        |
 Parent Class (B)
        ^
        |
 Child Class (C)
 Example: Animal -> Mammal -> Dog
 
'''

class Vehical :
    company = "BMW Motors"

    def __init__(self, n_wheel, n_seats, mileage):
        print("\ninit of vehicals\n")
        self.n_wheel = n_wheel
        self.n_seats = n_seats
        self.mileage = mileage
        
    def get_details(self):
        return f"This vehical has {self.n_wheel} wheel, {self.n_seats} seats and provide the mileage of {self.mileage}"


class Car(Vehical) : # single inheritance here Cars is child & Vehicals is Parent class
        
        model = "BMW M5"
        
        def __init__(self, car_type, drive_type, wheel, seats, mileage ):
            print("init of Cars")
            self.car_type = car_type
            self.drive_type = drive_type
            super().__init__(wheel, seats, mileage)
        
        def display_info(self):
            print(f"Car type : {self.car_type}")
            print(f"Drive type: {self.drive_type}")
            
class ElectricCar(Car) :
    def __init__(self, car_type, drive_type, wheel, seats, mileage, battery_capacity, distance_capacity):
        print("init of eletric car")
        self.battery_capacity = battery_capacity
        self.distance_capacity = distance_capacity
        super().__init__(car_type, drive_type, wheel, seats, mileage)
    
    def charge(self) :
        print(f"Charging the to {self.battery_capacity}")

ec1 = ElectricCar("Suv", "Manual", 4, 8, 20, 80, 400)
ec1.charge()
ec1.display_info()
print(ec1.get_details())

print("\n-----------------------\n")

print(ec1.__dict__)

print("\n-----------------------\n")

# help(ElectricCar)


print("\n-----------------------\n")
print("\n-----------------------\n")


class Animal: # Grandparent
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print(f"{self.name} is breathing.")

class Mammal(Animal): # Parent, inherits from Animal
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color
    
    def give_birth(self):
        print(f"{self.name} gives birth to live young.")

class Dog(Mammal): # Child, inherits from Mammal
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def bark(self):
        print(f"{self.name} ({self.breed}) says Woof!")


my_dog = Dog("Buddy", "Golden", "Golden Retriever")
my_dog.breathe() # Inherited from Animal
my_dog.give_birth() # Inherited from Mammal
my_dog.bark() # Specific to Dog
print(f"My dog's fur color: {my_dog.fur_color}")