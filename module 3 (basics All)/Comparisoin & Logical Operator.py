Python 3.15.0a8 (tags/v3.15.0a8:55ea59e, Apr  7 2026, 14:21:25) [MSC v.1950 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# comparision Operator

# == , != , < , > , <= , >=

n1 = 100
n2 = 10
n3 = 10

n1 == n2
False
n2 == n3
True

'python' == 'python'
True
'Python' == 'python'
False


n1 != n2
True
n2 != n3
False

'python' != 'python'
False
'Python' != 'python'
True

n1 > n2
True
n1 = 100
n2 = 99
n3 = 100
n1 > n2
True
n1 > n3
False
n1 >= n2
True
n1 >= n3
True


n1 < n2
False
>>> n1 < n3
False
>>> n1 <= n2
False
>>> n1 <= n3
True
>>> True
True
>>> 
>>> 
>>> # Logical Operator
>>> 
>>> # and  , or  ,  not
>>> 
>>> name = "vivek"
>>> age = 21
>>> 
>>> name == "vivek" and age == 21
True
>>> name == "vivek" and age == 18
False
>>> name == "akash" and age == 21
False
>>> name == "viveK" and age <= 15
False
>>> 
>>> 
>>> name == "vivek" or age == 21
True
>>> name == "vivek" or age < 21
True
>>> name == "Vivek" or age >= 21
True
>>> name == "viVek" or age < 21
False
>>> 
>>> not name == "vivek"
False
>>> not name == "viveK"
True
