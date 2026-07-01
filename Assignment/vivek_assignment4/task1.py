'''
Task 1: Read a File and Handle Errors
Problem Statement: Write a Python program that:
1. Opens and reads a text file named sample.txt.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.
'''

# File exists case
print("If sample.txt file exist")
file_name = "sample.txt"                # File name

try:                                    # Start try block
    with open(file_name, "rt") as fh:   # Open file in read mode
        data1 = fh.readline()           # Read first line
        data2 = fh.readline()           # Read second line
        print("\nReading file content:")  # Print heading
        print(f"""Line 1: {data1}Line 2: {data2}""")  # Display file content

except FileNotFoundError:               # Handle missing file
    print(f"Error: The file '{file_name}' was not found.")  # Print error


# File does not exist case
print("\nIf sample3.txt file does not exist\n")

file_name = "sample3.txt"               # File name

try:                                    # Start try block
    with open(file_name, "rt") as fh:   # Open file in read mode
        data1 = fh.readline()           # Read first line
        data2 = fh.readline()           # Read second line
        print("Reading file content:")  # Print heading
        print(f"""Line 1: {data1}Line 2: {data2}""")  # Display file content

except FileNotFoundError:               # Handle missing file
    print(f"Error: The file '{file_name}' was not found.")  # Print error