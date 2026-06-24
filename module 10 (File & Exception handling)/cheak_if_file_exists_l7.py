'''
os.path.exists() ==> in os module there is an exists()  
it is straight forword way of checking if the file exits or not

pathlib.path.exists() ==> in pathlib module there is an exists()

'''
# os.path.exists() ==> in os module there is an exists()  

import os as o

file_name  = "practicel1.txt"
if o.path.exists(file_name):
    print("file exists")
else:
    print("file does not exists")
    
import os as o

file_name  = "D:/python tutedude/module 10 (File & Exception handling)/created_file_l5.txt"
# D:\python tutedude\module 10 (File & Exception handling)\created_file_l5.txt (change the '\' --> '/')


if o.path.exists(file_name):
    print("file exists")
else:
    print("file does not exists")
    
    
# pathlib.path.exists() ==> in pathlib module there is an exists()

from pathlib import Path
file_name  = Path("practice_l7.txt",'xt')

# D:\python tutedude\module 10 (File & Exception handling)\created_file_l5.txt (change the '\' --> '/')


if file_name.exists():
    print("file exists.  Cannot create a file")
else:
    print("file does not exists.  Creating it")
    fh = open("practice_l7.txt",'xt')
    fh.write("Some containt")
    fh.close
    
    