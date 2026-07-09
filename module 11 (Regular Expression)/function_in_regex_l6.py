# match() ==> it use to find the pattern at the beginning of the string

import re
s1 = "We are learning regex in Python"
pat = r"[A-Z][a-z]"
m_obj = re.match(pat,s1)
print(m_obj) # <re.Match object; span=(0, 2), match='We'>

s1 = "We are learning regex in Python"
pat = r"[a-z]{3}"
m_obj = re.match(pat,s1)
print(m_obj) # None

ph_no = "ak-1234567890, vk-0987654321, ck-9021345678"
pat = r"[0-9]{10}"
m_obj = re.search(pat, ph_no)
print(m_obj) # <re.Match object; span=(3, 13), match='1234567890'>


# findall() ==> it will find all the occurrences and put all the data as object in a list

ph_no = "ak-1234567890, vk-0987654321, ck-9021345678"
pat = r"[0-9]{10}"
m_obj = re.findall(pat, ph_no)
print(m_obj) # ['1234567890', '0987654321', '9021345678']


ph_no = "ak-1234567890, vk-0987654321, ck-9021345678, gk-1234567"
pat = r"[0-9]{10}"
m_obj = re.findall(pat, ph_no)
print(m_obj) # ['1234567890', '0987654321', '9021345678']

ph_no = "ak-1234567890, vk-0987654321, ck-9021345678, gk-1234567"
pat = r"[0-9]+"
m_obj = re.findall(pat, ph_no)
print(m_obj) # ['1234567890', '0987654321', '9021345678', '1234567']

ph_no = "ak-1234567890, vk-0987654321, ck-9021345678, gk-1234567, Python3.13.5"
pat = r"[0-9]+"
m_obj = re.findall(pat, ph_no)
print(m_obj) # ['1234567890', '0987654321', '9021345678', '1234567', '3', '13', '5']

# fatch all phone no. the ph no are exact 7 digit and shoulde not be exceed 10 digit
ph_no = "ak-1234567890, vk-0987654321, ck-9021345678, gk-1234567, Python3.13.5"
pat = r"[0-9]{7,10}"
m_obj = re.findall(pat, ph_no)
print(m_obj) # ['1234567890', '0987654321', '9021345678', '1234567']

# fatch all phone no. the ph no are at least 7 digit 
ph_no = "ak-1234567890, vk-0987654321, ck-9021345678, gk-1234567, Python3.13.5"
pat = r"[0-9]{7,}" # 7 or more
m_obj = re.findall(pat, ph_no)
print(m_obj) # ['1234567890', '0987654321', '9021345678', '1234567']

# finditrt() ==>

ph_no = "ak-1234567890, vk-0987654321, ck-9021345678, gk-1234567, Python3.13.5"
pat = r"[0-9]{7,10}" 
m_obj = re.finditer(pat, ph_no)
for m in m_obj :  
    print(m) 
    
'''
output 
<re.Match object; span=(3, 13), match='1234567890'>
<re.Match object; span=(18, 28), match='0987654321'>
<re.Match object; span=(33, 43), match='9021345678'>
<re.Match object; span=(48, 55), match='1234567'>
'''