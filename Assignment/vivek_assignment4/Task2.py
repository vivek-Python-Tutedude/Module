'''
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1. Takes user input and writes it to a file named output.txt.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.

'''
file_name = "sample1.txt"                     # Create a variable to store the file name

with open(file_name, "wt") as fh:             # Open the file in write text mode 
        d1 = input("Enter text to write to file:")  # Take input from the user
        fh.write(d1)                          # Write the entered text into the file
        print(f"Data successfully written to {file_name}.\n")  # Display a success message

with open(file_name, "at") as fh:             # Open the file in append text mode
        d2 = input("Enter text to append to file:")  # Take another input from the user
        print(f"Data successfully append.\n") # Display append success message
        fh.write("\n" + d2)                   # Append the new text on the next line

with open(file_name, "rt") as fh:             # Open the file in read text mode
        print(f"Final content of {file_name}.")  # Display the file name
        data1 = fh.readline()                 # Read the first line from the file
        data2 = fh.read()                     # Read the remaining content of the file

print(data1 + data2)                          # Print the complete content of the file

