'''
# importing all module
import arithmatic_l14 as a
n1 = 100
n2 = 15
a = 45
b = 63
a.add(n1,n2)
# a.add(a, b) # it gives error because we have to pass n1 and n2 variabel not a and b
n = 49
a.sqroot(n)
# a.sqroot(a) # it gives error because we have to pass n variabel not a 

'''
# importing only sqroot function in that module
from arithmatic_l14 import sqroot

sqroot(n = 100)
# add(n1 = 4, n2 = 7) # it gives error because we importing only the sqroot()