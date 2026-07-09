import re

ph_no = "ak-1234567890, vk-0987654321, ck-9021345678"
pat  =r"\d{10}"
m_obj = re.findall(pat, ph_no)
print(m_obj) # ['1234567890', '0987654321', '9999999999']

ph_no = "ak-1234567890, vk-0987654321, ck-9021345678"
pat  =r"\d{10}"
pat_comp = re.compile(pat) #
'''
when we are using same pattern use for multiple searches in multiple string 
in that case if we compile it once and we use again it save the time and it optimizes the code
'''
print(pat_comp) # re.compile('\\d{10}')
print(type(pat_comp)) # <class 're.Pattern'>

m_obj = re.findall(pat_comp, ph_no)
print(m_obj)

with open("student_details_l8.txt", "rt") as fh :
    data = fh.read()
    
print(data)
print(type(data))

m_obj = re.finditer(pat_comp, data) # findall will complie the objectbecause of that we use finditer
for m in m_obj :
    print(m)
'''
output
<re.Match object; span=(18, 28), match='1234567890'>
<re.Match object; span=(47, 57), match='0987654321'>
<re.Match object; span=(76, 86), match='9999999999'>
'''



