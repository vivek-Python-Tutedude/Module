import re

with open("student_details_l9.txt", "rt") as fh :
    data = fh.read()
    
pat = r"[A-z0-9_.-]+[@][A-z]+[.][a-z]+"
match_obj = re.finditer(pat, data)

for m in match_obj:
    print(m)
    
print("\n")
# valid emails
pat = r"[A-z][A-z].[a-zA-Z0-9]+[\w.-][@][a-z]+[.][a-z]+"
match_obj = re.finditer(pat, data)
for m in match_obj:
    print(m)