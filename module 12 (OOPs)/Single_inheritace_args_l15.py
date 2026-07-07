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

c1 = Car("Suv", "Manual", 4, 8, 20)

# we pass all the value like above

print(f"Car type = {c1.car_type}")
print(f"Drive type = {c1.drive_type}")
print(f"Model = {c1.model}")

print(f"Seats = {c1.n_seats}")
print(f"Wheels = {c1.n_wheel}")
print(f"Mileage = {c1.mileage}")
print(c1.get_details())