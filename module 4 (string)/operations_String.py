'''s1 = "python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))

lan = "python"
ver = "3.14.4"
print(lan + ver)
'''

s1 = "vivek"
print(s1 + " satpute")
# print(s1 - v) we can't remove the v like this
print(s1 * 5)  # in string '*' is repetation operator



# membership operator
# 1] in

s1 = "vivek Ananda satpute"
print("vivek" in s1)
print('z' in s1)

# 2] not in

s1 = "vivek Ananda satpute"
print("vivek" not in s1)
print('z' not in s1)

# "in" & "not in" are case sensitive

#comparison of string

print("vivek" == "vivek")
print("Vivek" == "vivek")
print("vivek " == "vivek")

# strip() => remove uneccarey space from string
s1 = "     vivek          "
print(s1.strip())
s2 = "      vivek           s" #remove uneccarey space 
print(s2.strip())

print(s1.strip() == "vivek")

s3= "     vi    vek          "
print(s3.strip())


# repalce() => it wii not change the orignal string

s1 = "vivek satpute"
print(s1)
print(s1.replace("vivek","akash"))
print(s1)

s1 = "vivek satpute"
print(s1)
print(s1.replace("v","a"))
print(s1)

s1 = "vivek satpute"
print(s1)
print(s1.replace("v","a",1))
print(s1)


