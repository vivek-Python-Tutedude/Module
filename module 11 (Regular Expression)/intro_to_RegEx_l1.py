'''
Regular Expression (RegEx) ==> It is the special sequence of chcracter that defines a pattern for doing complex string matching functionality
Re module ==> it is useful for search operation & also it provides mete character or special symbols and quntifiers

'''

msg = "The current Python version is 3.13"
print("Python" in msg)
print("13" in msg)
print("14" in msg)

print(msg.find('3.13'))
print(msg.find("Python"))

print("\n")


import re

'''
re.search(regex_pattern, string) ==> if match found search function returns the match object else it returns None

'''

msg = "The current Python version is 3.13. Other previous version are 3.12, 3.11, 3.10."
match_obj = re.search('13', msg)
print(match_obj) # <re.Match object; span=(32, 34), match='13'>  # in this 34 is excluded
# span ==> It gives the information about from where to where this pattern is present in the msg

if re.search('13', msg) :
    print("found")
else :
    print("not found")