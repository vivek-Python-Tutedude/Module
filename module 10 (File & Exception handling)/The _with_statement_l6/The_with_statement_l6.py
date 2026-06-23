'''
with statement :- It will simplifies resource managment by automatically handling the setup and cleanup task
(It ensuers that the resources are properly released even though there are erros in the code it makes the code clean)
# with ensures automatic file closure after reading the file using the read function 
# If there is an error the 'with' will ensure that before program terminates file will be closed 
# after that the program will be terminates
# in normally the if there is an error the program will be terminate before closing the file

'''

'''

fh = open("practicel1.txt","rt")
containts = fh.read()
fh.close()
print(containts)

'''

with open("practicel1.txt",'rt') as fh :
    containt = fh.read()
    
print(containt)

with open("practice_l6.txt",'xt') as fh :
    fh.write("New file is created\n")
    fh.write("Bye!")
    
print(containt)