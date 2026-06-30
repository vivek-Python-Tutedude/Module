'''
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1. Opens and reads a text file named sample.txt.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

'''

import os as o                          # Import os module

file_name = "sample3.txt"               # Store file name
try:                                    # Start exception handling
    o.path.exists(file_name)            # Check if file exists
    with open(file_name, "rt") as fh:   # Open file in read mode
        data1 = fh.readline()           # Read first line
        data2 = fh.readline()           # Read second line
        print("Reading file content:")  # Print heading
        print(f"""Line 1: {data1}Line 2: {data2}""")  # Print file content
        fh.close()                      # Close file
        
except FileNotFoundError:               # Handle file not found error
    print(f"Error: The file'{file_name}' was not found.")  # Print error message
