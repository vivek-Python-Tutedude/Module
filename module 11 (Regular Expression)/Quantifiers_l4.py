'''
Quantifier ==> It tell how match quantity of a particular special character we want to match

'''

import re

msg = "The current Python version is 3.13. Other previous version are 3.12, 3.11, 3.10."

pat = r"[a-z]{4}" # 4 small char
match_obj = re.search(pat, msg) # <re.Match object; span=(4, 8), match='curr'>
print(match_obj)

pat = r"[A-Z][a-z]{4}" # 1 capital 4 small char
match_obj = re.search(pat, msg) # <re.Match object; span=(12, 17), match='Pytho'>
print(match_obj)

pat = r"[A-Z][a-z]{2,5}" # 1 capital and 2 or upto 4 small char
match_obj = re.search(pat, msg) # <re.Match object; span=(0, 3), match='The'>
print(match_obj)

# + ==> it matches 1 or more repetation of previous pattern

pat = r"[A-Z][a-z]+" # 1 capital and 1 or more small char
match_obj = re.search(pat, msg) # <re.Match object; span=(0, 3), match='The'>
print(match_obj)

# ? ==> 0 or 1 repetation of the previous pattern

pat = r"[A-Z][a-z]?" 
match_obj = re.search(pat, msg) # <re.Match object; span=(0, 2), match='Th'>
print(match_obj)

# * ==> 0 or more repetation of the previous pattern

pat = r"[A-Z][a-z]*" 
match_obj = re.search(pat, msg) # <re.Match object; span=(0, 3), match='The'>
print(match_obj)

