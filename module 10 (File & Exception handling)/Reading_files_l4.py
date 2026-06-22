'''
read a file
read() ==> reads the containts of a file
if file is text file it will read as string

'''
file_handler = open("practicel1.txt", "rt")
print(file_handler)
lines = file_handler.readlines() # it gives all the lines in the form of list
# it will give newline as \n 

'''
line1 = file_handler.readline() # it gives each line
line2 = file_handler.readline()
line3 = file_handler.readline()
line4 = file_handler.readline()
line5 = file_handler.readline()
'''
# content1 = file_handler.read(10) # this read first 10 characters (space will be also cosider)

# content = file_handler.read() # reading all the content in file

# closing a file ==> close()

file_handler.close()
file_handler.close()
# we can close file multiple times 
# but after closing the file we can't do read or write operation

# print(content)
# print(type(content))

# print(content1)
# print(type(content1))

# print(line1)
# print(type(line1))
'''
print(f"Line1 : {line1}") # after each line it give \n 
print(f"Line2 : {line2}")
print(f"Line3 : {line3}")
print(f"Line4 : {line4}") # empty string ==> file is reached end of file (EOf)
print(f"Line5 : {line5}")

'''

print(f"lines = {lines}")
print(type(lines))

for line in lines : # printing line wise 
    print(line.rstrip('\n')) # rstrip()is used to remove uneccsary spaces