'''
Task 2: Demonstrate List Slicing
Problem Statement: Write a Python program that:
1. Creates a list of numbers from 1 to 10.
2. Extracts the first five elements from the list.
3. Reverses these extracted elements.
4. Prints both the extracted list and the reversed list.
'''

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]      # Create a list of numbers
print(f"Original list: {num}")          # Display the original list

num2 = num[:5:1]                        # Extract the first five elements
print(f"Extracted first five elements: {num2}")  # Display extracted list

print(f"Reversed extracted elements: {num2[::-1]}")  # Display reversed extracted list

# print(f"Reversed extracted elements: {list(reversed(num2))}")  # Alternative method to reverse the list