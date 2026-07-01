'''
Task 1: Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:
1. Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student’s name is not found, display an appropriate message.
'''

dic = {"Alice": 92, "Vivek": 98, "Akash": 94.6}   # Create a dictionary

search = input("Enter the student's Name: ")      # Take student name as input

if search in dic:                                 # Check if name exists
    print(f"{search}'s Marks = {dic[search]}")    # Display student's marks
else:                                             # If name is not found
    print("Student not found")                    # Display error message