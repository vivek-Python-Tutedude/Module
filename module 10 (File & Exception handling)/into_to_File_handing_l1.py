'''
files are handling in 2 ways
1] text files  2] Binary files
In python text files are store the data in the form of character (normal text file)
In python Binary files are store the data in the form of bytes (image file ,audio & video files)

# file operation ==> read, write, edit, create, add, open, close, delete

# open file in python
# open(file_nm, mod_to_open)
# modes ==> r = read, x = create, w = write | overwrite, a = append, t = (open) working on text file
            b = (open) working with binary file
'rt' are default mode
'''

file_handler = open("practicel1.txt", "rt")
print(file_handler)

# closing a file ==> close()
file_handler.close()
file_handler.close()
# we can close file multiple times 
# but after closing the file we can't do read or write operation 