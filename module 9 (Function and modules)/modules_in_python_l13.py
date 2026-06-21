'''
modules == Module is a file it containing defination and statement
any python file having python code in it with the extension of .py file is a module

2 typrs of module 
1] bulit in module 2] user define module
1] bulit in module ==> math, random, datetime, ...
  
'''

# how to import module
# syntax ==> import module_nm
# for importing only few function / variable : from module_nm import f1, f2, f3
# sybtax to creat an alias for the module that is imported: import module_nm as alias_nm

import math

# calculate sqr root of no
n = 100
op = math.sqrt(n) # module_nm.function_nm(arg1, arg2, arg3 ....)
print(f"sqr root of {n} is = {op}")

# calculating are of a circle ==> pi * r ** 2  (pi * r^2)
r = 5
area = math.pi * (r ** 2) # we imported a variable pi
print(f"Area of circle with radius {r} is = {area}")

from random import randint # we can impor sepcific function in that module

val = randint(1, 6)
print(val)

# sybtax to creat an alias for the module that is imported: import module_nm as alias_nm
import datetime as dt
t = dt.time(5, 30, 30)
print(t)
