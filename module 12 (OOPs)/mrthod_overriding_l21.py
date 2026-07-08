'''
Overriding Methods
 A derived class can provide its own specific implementation for a method that is
already defined in its base class. This is called method overriding.

 When an overridden method is called on an object of the derived class, the derived
class's versio

Usage with Overridden Methods:
You can use super() to call the parent's version of an overridden method, and then add
specific logic in the child.

'''

class Employee : 
    def working_hr(self) :
        return 45
    
class Intern(Employee) :
    
    def working_hr(self):
        return 40

e1 = Employee()
print("Employee's working hr = ",e1.working_hr())

i1 = Intern()
print("Intern working hr = ",i1.working_hr())

print("----------------------")

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Generic animal sound")
        
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
        
    def make_sound(self): # Overriding make_sound
        print(f"{self.name} barks loudly!")
        
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed
        
    def make_sound(self): # Overriding make_sound
         print(f"{self.name} says Meow!")
         
         
animal1 = Animal("Leo", "Lion")
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "Siamese")

animal1.make_sound() # Calls Animal's make_sound
dog1.make_sound() # Calls Dog's make_sound
cat1.make_sound() # Calls Cat's make_sound

print("----------------------------")

class Vehicle:
    def __init__(self, brand):
         self.brand = brand
         
    def start_engine(self):
         print(f"{self.brand} engine starts.")
         
    def display_info(self):
         print(f"Brand: {self.brand}")
         
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand) # Call parent's __init__
        self.model = model
        
    def start_engine(self):
    # Call parent's start_engine and then add car-specific logic
        super().start_engine()
        print(f"{self.model} specific car checks complete.")
        
    def display_info(self):
        super().display_info() # Call parent's display_info
        print(f"Model: {self.model}")
        
        
my_car = Car("Toyota", "Camry")
my_car.start_engine()

print("-" * 20)
my_car.display_info()