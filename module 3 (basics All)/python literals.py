Python 3.15.0a8 (tags/v3.15.0a8:55ea59e, Apr  7 2026, 14:21:25) [MSC v.1950 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = -100
>>> type(a)
<class 'int'>
>>> 100
100
>>> 10.2
10.2
>>> a = -10.0
... type(a)
SyntaxError: multiple statements found while compiling a single statement
>>> b = -100
... type(b)
SyntaxError: multiple statements found while compiling a single statement
>>> 10.0
10.0
>>> b = -100
... type(b)
SyntaxError: multiple statements found while compiling a single statement
>>> b = -10.0
>>> type(b)
<class 'float'>
>>> 'vivek'
'vivek'
>>> "vivek"
'vivek'
>>> '''vivek
... how are you'''
'vivek\nhow are you'
>>> """vivek
... what are you doing"""
'vivek\nwhat are you doing'
>>> true
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> True
True
>>> False
False
bool a = 0
SyntaxError: invalid syntax
bool c = True
SyntaxError: invalid syntax
d = True
type(d)
<class 'bool'>
