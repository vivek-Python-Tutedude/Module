a = float(input("Enter the first side:"))
b = float(input("Enter the secound side:"))
c = float(input("Enter the third side:"))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 #square root = 0.5 by formula
print("area of triangel : ",round(area,2))

