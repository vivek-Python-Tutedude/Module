
fh = open("practice_l7.txt",'rt')
con = fh.read()
fh.close()
print(con)
# io.UnsupportedOperation: not readable
'''

# if file does not exists it gives error
fh = open("xyz.txt",'wt')
con = fh.read()
fh.close()
print(con)

'''
'''
# we can't use read mode And use write() it gives error 

fh = open("practice_l7.txt",'rt')
con = fh.write()
fh.close()
print(con)
TypeError: TextIOWrapper.write() takes exactly one argument (0 given)

'''

'''
# If we use the write mode and try to use the read function it cause error and also delete the containt from the file

fh = open("practice_l7.txt",'wt')
con = fh.read()
fh.close()
print(con)
# error ==> io.UnsupportedOperation: not readable

'''
'''

fh = open("practice_l7.txt",'xt')
con = fh.write("Some conatint")
fh.close()
print(con)
# FileExistsError: [Errno 17] File exists: 'practice_l7.txt'

'''