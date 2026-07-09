# sub() ==> it is used to subsitute a pattern with another string or substring

import re

s1 = "Sunday, Monday, Tuesday, Monday, Sunday"
pat = 'Sunday'
replacement = "Friday"
result = re.sub(pat, replacement, s1)
print(result) #  Friday, Monday, Tuesday, Monday, Friday

result = re.sub(pat, replacement, s1, count = 1)
print(result) #  Friday, Monday, Tuesday, Monday, Sunday

s1 = "Sunday, Monday, Tuesday, Monday, Sunday"
pat = r"S[A-z]+"
replacement = "Friday"
result = re.sub(pat, replacement, s1)
print(result) # Friday, Monday, Tuesday, Monday, Friday

msg = """We are learning re. using RE, we can search for a pattern in agiven string.
Using the sub(), we can replace the pattern with a given string as well."""

pat = r"\bre\b"  

''' \b is used for word boundary it will help to identify exact word like in above statement
 (are) consist re so \b will prevent to replacement'''
 
replacement = "Regular Expression"
result = re.sub(pat, replacement, msg)
print(result)

'''
output
We are learning Regular Expression. using RE, we can search for a pattern in agiven string.
Using the sub(), we can replace the pattern with a given string as well.
'''
# we have to replace both re and RE

msg = """We are learning re. using RE, we can search for a pattern in agiven string.
Using the sub(), we can replace the pattern with a given string as well."""

pat = r"\bre\b"  
replacement = "Regular Expression"
result = re.sub(pat, replacement, msg, flags = re.IGNORECASE)
print(result) 
'''
output
We are learning Regular Expression. using Regular Expression, we can search for a pattern in agiven string.
Using the sub(), we can replace the pattern with a given string as well.

'''

phno = "+91-1234567890, +91-0987654321"
pattern = r"[+-]"
rep = ""
result = re.sub(pattern, rep,phno,)
print(result) # 911234567890, 910987654321