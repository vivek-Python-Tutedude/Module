Python 3.15.0a8 (tags/v3.15.0a8:55ea59e, Apr  7 2026, 14:21:25) [MSC v.1950 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num1 = 100
num1
100


print(num1)
100

print(200)
200
nsme = "vivek"
print(name)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined. Did you mean: 'nsme'?
print(nsme)
vivek
age = 21
print(age)
21
print(nsme,age)
vivek 21
print(nsme, age)
vivek 21

print(10,20,30,40)
10 20 30 40


print(10,20,30,40,sep =" ")
10 20 30 40


print(10,20,30,40,sep = ",")
10,20,30,40

print(10,20,30,40,sep = "@")
10@20@30@40
print(10,20,30,40,sep = "vivek")
10vivek20vivek30vivek40


print("vivek")
vivek

print("vivek')
      
SyntaxError: unterminated string literal (detected at line 1)


n1 = 100
      
n2 = 200
      
result = n1 + n2
      
print(n1,n2,result)
      
100 200 300
>>> 
>>> 
>>> # Addition of 100 and 200 is 300
...       
>>> print("Addition of",n1,"and",n2,"is",result)
...       
Addition of 100 and 200 is 300
>>> 
>>> 
>>> name = 'vivek'
...       
>>> age = 21
...       
>>> print(name,age)
...       
vivek 21
>>> 
>>> # Name: vivek, Age: 21
...       
>>> print("Name:",name,"Age")
...       
Name: vivek Age
>>> print("Name:",name,"Age:",age)
...       
Name: vivek Age: 21
>>> 
>>> 
>>> day = 04
...       
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> day = 4
...       
>>> month = 11
...       
>>> year = 2005
...       
>>> # 4/11/2005
...       
>>> print(day,month,year,sep = "/")
...       
4/11/2005
