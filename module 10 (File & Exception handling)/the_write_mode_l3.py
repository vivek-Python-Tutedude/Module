'''
w mode ==> open the file for writing or overwriting the file
overwrite ==> it will delete previous content of file then it will write
# preveous content will be lost
# if file does not exist "w" mode create a file
it behave like 'x' mode
'''
fh = open("createedfile_l2.txt", "wt")
fh2 = open("createedfile_l3.txt", "wt")

fh.write("This file is overwriten by the 'w' mode in python. \n")
fh.write("have a nice day!")
fh.close()

fh2.write("This file is overwriten by the 'w' mode in python. \n")
fh2.write("have a nice day!")
fh2.close()