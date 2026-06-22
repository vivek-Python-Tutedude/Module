'''
creating a file

'''
# x mode ==> create a file

fh = open("createedfile_l2.txt", "xt")

# writing into a file
# write("content")
fh.write("This file is created using the 'x' mode in python. \n")
fh.write("Next line.")

# close the file
fh.close()

# fh.write() we can't write or read in file after closing
## if we run this program 2nd time it gives error beacuse using x mode we can create file but
# when we 2nd time run file is file is already created