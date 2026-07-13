Python 3.15.0a8 (tags/v3.15.0a8:55ea59e, Apr  7 2026, 14:21:25) [MSC v.1950 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string
>>> 
>>> s1 = 'vivek'
>>> s1
'vivek'
>>> s2 = "vivek"
>>> s2
'vivek'
>>> s3  = '''vivek
... satpute'''
>>> s3
'vivek\nsatpute'
>>> s4 = """vivek
... satpute"""
>>> s4
'vivek\nsatpute'
>>> type(s4)
<class 'str'>
>>> 
>>> #ien
>>> s5 = "vivek satpute
SyntaxError: unterminated string literal (detected at line 1)
>>> s5 = "vivek satpute"
>>> len(s5)
13
>>> 
>>> len(s2)
5
>>> 
>>> 
>>> #index
>>> s7 = "vivek satpute"
>>> s7[5]
' '
>>> s7[9]
'p'
>>> s7[0]
'v'
>>> s7[14]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s7[14]
IndexError: string index out of range

 s8 = 'akash satpute'
 
SyntaxError: unexpected indent
s7 = 'akash'
s7 = 'akash satpute'
s7[-1]
'e'
s7[-12]
'k'


#concatenation
s1 = "vivek"
s2 = "satpute"
s3 = s1 + ' ' + s2
s3
'vivek satpute'
