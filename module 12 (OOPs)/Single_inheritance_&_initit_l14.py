'''
Single-Level Inheritance
Definition: The simplest form of inheritance, where a derived class inherits from only
one base class.
 Relationship: Parent-Child.
 Diagram:
 Base Class
 ^
 |
 Derived Class

'''

class Vehical :
    company = "BMW Motors"

    def __init__(self, n_wheel, n_seats, mileage):
        print("\ninit of vehical\n")
        self.n_wheel = n_wheel
        self.n_seats = n_seats
        self.mileage = mileage
        
    def get_details(self):
        return f"This vehical has {self.n_wheel} wheel, {self.n_seats} seats and provide the mileage of {self.mileage}"


class Car(Vehical) : # single inheritance here Car is child & Vehical is Parent class
    pass


# c1 = Car() # TypeError: Vehical.__init__() missing 3 required positional arguments: 'n_wheel', 'n_seats', and 'mileage'
# it gives error because parent class attributes need to be accessed by the child class so they need to initalize 

c1 = Car(4, 7, 15)
print(f"Seats = {c1.n_seats}")
print(f"Wheels = {c1.n_wheel}")
print(f"Mileage = {c1.mileage}")
print(c1.get_details())
# child class has access of all the attributes and method of parent class

# if we have init() of only parent class we have to pass argumrnt defined in init() of paarent class


print("\n-------------------------------\n")


class Vehicals :
    company = "BMW Motors"

    def __init__(self, n_wheel, n_seats, mileage):
        print("\ninit of vehicals\n")
        self.n_wheel = n_wheel
        self.n_seats = n_seats
        self.mileage = mileage
        
    def get_details(self):
        return f"This vehical has {self.n_wheel} wheel, {self.n_seats} seats and provide the mileage of {self.mileage}"


class Cars(Vehicals) : # single inheritance here Cars is child & Vehicals is Parent class
        
        model = "BMW M5"
        
        def __init__(self, car_type, drive_type ):
            print("init of Cars")
            self.car_type = car_type
            self.drive_type = drive_type

c1 = Cars("SUV", "Manual")

print(f"Car type = {c1.car_type}")
print(f"Drive type = {c1.drive_type}")
print(f"Model = {c1.model}")

# if we have init() method of both child and parent class so we have to pass the argument according to the 
# child class as per above & if we have to access the attributes & method of child class At that time,
# we have to explicitly call the init() of parent 
# if we don't call the explicitly and try to access it gives error like below
# print(f"Mileage = {c1.mileage}")   # AttributeError: 'Cars' object has no attribute 'mileage'



print("\n-------------------------------\n")


class Vehicalss :
    company = "BMW Motors"

    def __init__(self, n_wheel, n_seats, mileage):
        print("\ninit of vehicals\n")
        self.n_wheel = n_wheel
        self.n_seats = n_seats
        self.mileage = mileage
        
    def get_details(self):
        return f"This vehical has {self.n_wheel} wheel, {self.n_seats} seats and provide the mileage of {self.mileage}"


class Carss(Vehicalss) : # single inheritance here Cars is child & Vehicals is Parent class
        
        model = "BMW M5"
        
        def __init__(self, car_type, drive_type ):
            print("init of Cars")
            self.car_type = car_type
            self.drive_type = drive_type
# 1st method # Vehicalss.__init__(self, 4, 8, 23) # when we call the any instance method by class name we have to pass the obj
# 2nd method
            super().__init__(2, 3, 50)

# super function is actually used to refer to the parent class & we are calling the init of super class it means calling the parent class 
# main adventage of super is we don pass the obj it will pass 1st args as obj automatically

c1 = Carss("SUV", "Manual")

print(f"Car type = {c1.car_type}")
print(f"Drive type = {c1.drive_type}")
print(f"Model = {c1.model}")

print(f"Seats = {c1.n_seats}")
print(f"Wheels = {c1.n_wheel}")
print(f"Mileage = {c1.mileage}")
print(c1.get_details())