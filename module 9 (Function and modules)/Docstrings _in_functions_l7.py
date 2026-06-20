'''
Docstrings:- we use the document or  docstrings inside our function defination so that
anybody sees our function he can understand what is done inside the function
# it must be return in start of defination
'''

def func():
    """This is a Docstrigs
       we can write what the function does here
       :return : None 
    """
    return None

print(help(func)) # help()l:- it gives details about the any function
# print(help(print()))


def func():
    return None

    """This is a Docstrigs
       we can write what the function does here
       :return : None 
    """

help(func) # if we cannot write in first then we can't get docstring which is return in function

def division(n1, n2) :
    """Division

    Args:
        n1 (float): it is the numerator
        n2 (float): it is the denominator
        : return : (if n2 is zero) str (else n2 is non zero) n1 / n2
    """
    if n2 == 0 :
        return "cannot divide as denominator '0'"
    else :
        return n1 / n2
print("division =",division(12,7))    
help(division)