principle = float(input("Enter the principle ammount: "))
rate = float(input("enter the rate of interest: "))
time = float(input("Enter the time: "))

ammount = principle * ((1 + (rate / 100)) ** time)
am2 = principle * pow((1 + rate / 100 ),time)

print(ammount,am2)

ci = ammount - principle

print("compound interest is: ",ci)