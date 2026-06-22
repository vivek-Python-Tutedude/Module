'''
by taking user input & using the math module find 
1] square root of no
2] natural logarith
3] sine of the no
and display the result

'''
import math as m
n = int(input("Enter a number : ")) # taking the user input

sqr = m.sqrt(n) # usig the sqrt function calculate the square root of n
print(f"Square root: {sqr}")

nl = m.log(n)  # usig the lpg function calculate the natural Logarithm of n
print(f"Logarithm: {nl}")

s = m.sin(n)  # usig the Sin function calculate the Sine value of n
print(f"Sine: {s}")