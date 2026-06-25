import re
msg = "The current Python version is 3.13. Other previous version are 3.12, 3.11, 3.10."

# finding the 2 consicative digit in msg

match_obj = re.search("[0123456789][0-9]", msg) # [0123456789] == [0-9] both are same
print(match_obj)

match_obj = re.search("[0-9][0-9]", "house  no : 234 / A")
print(match_obj)

match_obj = re.search("[0-9][0-9][0-9]", "house  no : 034 / A")
print(match_obj)

match_obj = re.search("[0-9][0-9]", msg)
print(match_obj)

match_obj = re.search("[0-9][0-9][0-9]", msg)
print(match_obj)

match_obj = re.search("[0-9].[0-9][0-9]", msg)
print(match_obj)

match_obj = re.search("[0-9].[0-9]", msg) # <re.Match object; span=(30, 33), match='3.1'>
print(match_obj)

match_obj = re.search("[0-9].[0-9]", "house  no : 234 / A") # <re.Match object; span=(12, 15), match='234'>
print(match_obj)

# from above 2 example we get the dot (.) char is does not match with dot(.) only 
# it will also match with any character except newline char (\n)

msg1= "The year is 2026"

match_obj1 = re.search("[0-9].[0-9][0-9]", msg1) # <re.Match object; span=(12, 16), match='2026'>
print(match_obj1)

match_obj1 = re.search("...", msg1) # <<re.Match object; span=(0, 3), match='The'>
print(match_obj1) # 3 dots

match_obj1 = re.search(".....", msg1) # <re.Match object; span=(0, 5), match='The y'>
print(match_obj1) # 4 dots

match_obj1 = re.search("[0-9][.][0-9][0-9]", msg1) # None
print(match_obj1) 
# if we put the dot in [] then is will check only dot 

match_obj1 = re.search("[0-9][.][0-9][0-9]", msg) # <re.Match object; span=(30, 34), match='3.13'>
print(match_obj1)