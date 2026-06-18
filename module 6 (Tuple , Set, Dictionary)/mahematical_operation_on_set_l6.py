s1 = {"Eng", "Maths", "CS", "Phy", "Che","sanskrit"}
s2 = {"Eng", "Bio", "CS", "Phy", "Che","sanskrit", "geography"}
s3 = {"sanskrit", "geography","Phy","Che"}
s4 ={"Drawing"}
print(s1, type(s1))
print(s2, type(s2))

# common subject of s1 & s2 --> intersection
cm_sub = s1.intersection(s2)
print(cm_sub)
cm_sub = s1 & s2 & s3 # 2nd method
print("cm_sub: ", cm_sub)
cm_sub = s1 & s2 & s3 & s4 # Empty set == set()
print("cm_sub: ", cm_sub)

# all subject in of s1 and s2 --> union
al_sub = s1.union(s2)
print(al_sub)
al_sub = s1 | s2 | s3 | s4  # al_sub is also set  so it discad duplicate element
print("union: ", al_sub, type(al_sub))

# difference
s1 =  {10, 5, 9,}
print(s1, type(s1))
s2 = {19, 10, 3, 5}
print(s1, type(s1))

print(s1 - s2) # element of fs1 which not a part of fs2
print(s2.difference(s1)) # element of fs2 which not a part of fs1
print(s1 - s1) # empty set()