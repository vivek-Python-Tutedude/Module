'''
dunder name == __name__

__name__(variable) ==> this a special variable in python that help us to write an executable code inside our module
It is the special variable which is predefine in python which has valueset to module name  

'''
import arithmatic_l15
a = 100
out = arithmatic_l15.sqroot(a)
print(f"sqroot = {out}") 
#30 on next line sqroot = 10.0  # after executing code we get 30 which is in arithmatic_l15 this module
# the all code is excuted durin loding the code in memoey to avoid this we use  __name__
# ** above output is display when we remove  __name__ in arithmatic_l15 this module

'''
for ==> dunder_name_function_l15.py ==> __name__ = "__main__"
for ==> arithmatic_l15.py ==> __name__ = "arithmatic_l15"
'''

print(f"__name__value in dunder_name_function_l15.py is = {__name__}")
