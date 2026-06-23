'''
'a' modes ==> Append mode : it add the contents or appends the content to the end of the file
if file is does not exists then 'a' mode create a file

'''
fh = open("practicel1.txt", 'at')
fh.write("\nThis content has been wriiten using 'a' mode.\n")
fh.write("'a' mode is used it add the contents or appends the content to the end of the file")
fh.write("\nGoode bye!")
fh.close()

# using 'a' mode create a file and some containt in it

fh = open("created_file_l5.txt", 'at')
fh.write("\nThis content has been wriiten using 'a' mode.\n")
fh.write("'a' mode is used it add the contents or appends the content to the end of the file")
fh.write("\nGoode bye!")
fh.close()