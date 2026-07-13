Python 3.15.0a8 (tags/v3.15.0a8:55ea59e, Apr  7 2026, 14:21:25) [MSC v.1950 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num1 = 100
num1
100
type(num1)
<class 'int'>

num2 = float(num1)
num2
100.0
type(num2)
<class 'float'>


num2 = int(num2)
num2
100
type(num2)
<class 'int'>


num3 = 100
num3 = str(num3)
type(num3)
<class 'str'>
num3
'100'


num4 = 15.86
num4 = str(num4)
type(num4)
<class 'str'>
num4
'15.86'


num5 = '100'
num5 = int(num5)
type(num5)
<class 'int'>
num5
100


num6 = "58.36"
num6 = float(num6)
type(num6)
<class 'float'>
num6
58.36

num6 = "58"
num6 = float(num6)
type(num6)
<class 'float'>
num6
58.0


s1 = "vivek"
s1 = int{s1}
SyntaxError: invalid syntax
s1 = int(s1)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s1 = int(s1)
ValueError: invalid literal for int() with base 10: 'vivek'



lan = "python"
ver = 3.13
lan + ver
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    lan + ver
TypeError: can only concatenate str (not "float") to str
ver = str(ver)
lan + ver
'python3.13'


n1 = "100"
n2 = "123.5"
int(n1) + float(n2)
223.5



val = True
type(val)
<class 'bool'>
val = str(val)

bal
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    bal
NameError: name 'bal' is not defined. Did you mean: 'val'?
val
'True'
type(val)
<class 'str'>



val = "vivek"
val = bool(val)
val
True
type(val)
<class 'bool'>


vsl = 10086
vsl = bool(val)
vsl
True
type(val)
<class 'bool'>


vsl = 15.33
vsl = bool(vsl)
vsl
True
type(vsl)
<class 'bool'>


val = 0
val = bool(val)
type(bool)
<class 'type'>
val
False
type(val)
<class 'bool'>


bool(0.0)
False

bool(0.1)
True

bool(-163)
True
>>> 
>>> bool(-3.25)
True
>>> 
>>> bool(" ")#space
True
>>> bool("")#empty string
False
>>> bool('')
False
>>> bool('''''')
False
>>> bool("""""")
False
>>> 
>>> 
>>> bool(None)
False
>>> 
>>> val = True
>>> val = int(val)
>>> val
1
>>> type(val)
<class 'int'>
>>> 
>>> 
>>> val = False
>>> val = int(val)
>>> val
0
>>> type(val)
<class 'int'>
>>> 
>>> float(True)
1.0
>>> 
>>> float(False)
0.0
>>> 
>>> 
