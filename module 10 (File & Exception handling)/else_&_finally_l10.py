'''with open("my_file_l10.txt",'rt') as fh :
    data = fh.read()
    print(data)

    print("\n")
'''
try :
    with open("my_file_l10.txt",'rt') as fh :
        data = fh.read()
    print(data)
except FileNotFoundError:
    print("File does not exists")
    
print("\n")
    
try :
    with open("my_file_l10.txt",'rt') as fh :
        data = fh.read()
    print(data)
except FileNotFoundError as error: # error is an variable it stores the value in which printed in the terminal after running the code
    print("File does not exists")
    print(error,type(error))
    
print("\n")

# else block : it like if else if in try block there is an no error after that control moves towords to the else block
# else block will be only executed when the there is no error intry block


try :
    with open("practice_l7.txt",'rt') as fh : # intry block there is an no error file is exists
        data = fh.read()
except FileNotFoundError as error: # error is an variable it stores the value in which printed in the terminal after running the code
    print("File does not exists")
    print(error,type(error))
else :
    print(data)
    
# finally block:- finally block in the try except block is always executed irrespective of wether the error
#                 is happens or thr exception is there or raisedor not\
print("\n")
    
try :
    with open("practice_l7.txt",'rt') as fh : # in try block there is an no error file is exists
        data = fh.read()                      # so it will go to the else an then go in finally
        print("Try block")
        fh.close()
except FileNotFoundError as error: # error is an variable it stores the value in which printed in the terminal after running the code
    print("File does not exists")
    print(error,type(error))
else :
    print("else block")
    print(data)
finally :          # it will always executed
    print("Finally block") 
    
print("\n")
    
try :
    with open("m5.txt",'rt') as fh : # in try block there is an n error file is not exists
        data = fh.read()             # so it will go to the in finally block
        print("Try block")
except FileNotFoundError as error: # error is an variable it stores the value in which printed in the terminal after running the code
    print("File does not exists")
    print(error,type(error))
else :
    print("else block")
    print(data)
finally :          # it will always executed
    print("Finally block") 
    fh.close()
