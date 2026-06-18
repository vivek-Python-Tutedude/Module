# counting substring from a string
# count()
# string.count(substring)

s1 = "vivek vivek satpute"
s2 = "vivek"
print(s1.count(s2))
print(f"Occurrences of v is {s1.count("v")}")
print(f"Occurrences of put is {s1.count("put")}")
print(f"Occurrences of space  is {s1.count(" ")}")

print("\n")

#changing case of string
# upper(), lower(), title(), capatilize()

# upper() => it will convert lower letter into upper letter and number and spcial character remains same

s1 = "vivekSatpuTe"
print(s1.upper())

s2  = "vIvek 04/11"
print(s2.upper())

# lower() it will convert upper letter into lower letter and number and spcial character remains same

s1 = "VIVeKsATpUte"
print(s1.lower())

s2  = "vIvEk 04/11"
print(s2.lower())

# title() => - it will  covert each world of 1st letter upper and other letters of that word are remain lower 
# - And it also remove extra space 
# - And it also remove numbrs or special chracter in some cases as shown
s1 = "vivEk ananDa sAtpute"
print(s1.title())

s2 = "vivEk  04 ananDa 11       sAtpute 2005/"
print(s1.title())

s3 = " 10 + 0 - 1 * 3 /10"
print(s3.title())

s3 = "vive 10 + 0 - 1 * 3 /10  sat"
print(s3.title())

s3 = "viVek      04/11/2005 satpuTe"
print(s3.title())

print("\n")
# capitalize() => it will convert 1st letter of string is upper and other will remain lower

s1 = "vivEk ananDa sAtpute"
print(s1.capitalize())

s2 = "vivEk  04 ananDa 11       sAtpute 2005/"
print(s2.capitalize())


#starting and ending of string

# startswith()
# string.startswith(substring)
print("\n")


s1 = "vivek satpute"
s2 = "V"
print(s1.startswith("v"))
print(s1.startswith(s2))
print(s1.startswith("vivek"))
print(s1.startswith("viv"))

# endswith()
# string.endswith(substring)
print("\n")

s1 = "vivek satpute"
s2 = "E"
print(s1.endswith("e"))
print(s1.endswith(s2))
print(s1.endswith("ute"))
print(s1.endswith("satput"))