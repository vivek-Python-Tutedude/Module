import re

s1 = "Python is a programming language"

# raw string ==> if we put r like below it will treted as the raw string
# it we tell python don't read \n, \t (escape sequence)

pat = r"old\new" 
print(pat)

# [A-Z]  [a-z]

match_obj = re.search(pat, s1) # None
print(match_obj)

match_obj = re.search("[a-z][a-z]", s1) # <re.Match object; span=(1, 3), match='yt'>
print(match_obj)

match_obj = re.search(r"[A-Z][a-z][A-z]", s1) # <re.Match object; span=(0, 3), match='Pyt'>
print(match_obj) # [A-Z] ==> Only capital, [a-z] ==> only small, [A-z] ==> both capital and small
# [a-Z] ==> it gives error


# \d ==> it matches 1digit char. It is similar to [0-9]


print(pat)
s1 = "Python is a programming language. python3.14 is the current version"
pat = r"[a-z][a-z][a-z]" 

match_obj = re.search("[a-z][a-z][a-z]\d", s1) # <re.Match object; span=(37, 41), match='hon3'>
print(match_obj)

match_obj = re.search(pat + "\d", s1) # <re.Match object; span=(37, 41), match='hon3'>
print(match_obj)

# \D ==> It matches 1 non digit char

match_obj = re.search("[a-z][a-z][a-z]\D", s1) # <re.Match object; span=(1, 5), match='ytho'>
print(match_obj)

match_obj = re.search(pat + "\D", s1) # <re.Match object; span=(1, 5), match='ytho'>
print(match_obj)


#\s ==> It will matches any white space char or escape sequence like \t \n

s2 =  """Hi there
We are learning python
"""

match_obj = re.search("[a-z][a-z][a-z]\s", s2) # <re.Match object; span=(5, 9), match='ere\n'>
print(match_obj)

match_obj = re.search(pat + "\s", s2) # <re.Match object; span=(5, 9), match='ere\n'>
print(match_obj)

# \S ==> oppositeof \s . It mstches any char except space, \n, \t


match_obj = re.search("[a-z][a-z][a-z]\S", s2) # <re.Match object; span=(3, 7), match='ther'>
print(match_obj)

match_obj = re.search(pat + "\S", s2) # <re.Match object; span=(3, 7), match='ther'>
print(match_obj)


# \w ==> it matches alpha numecric char ==>[a-z], [A-Z], [0-9]

match_obj = re.search("[a-z][a-z][a-z]\w", s2) # <re.Match object; span=(3, 7), match='ther'>
print(match_obj)

match_obj = re.search(pat + "\w", s2) # <<re.Match object; span=(3, 7), match='ther'>
print(match_obj)

# \W ==> opposite of \w ==> it matches char Except ==>[a-z], [A-Z], [0-9]

match_obj = re.search("[a-z][a-z][a-z]\W", s2) # <re.Match object; span=(5, 9), match='ere\n'>
print(match_obj)

match_obj = re.search(pat + "\W", s2) # <re.Match object; span=(5, 9), match='ere\n'>
print(match_obj)