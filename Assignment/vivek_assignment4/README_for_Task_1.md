# 📂 Task 1 - Read a File and Handle Errors

## 📌 Problem Statement

Write a Python program that:

1. Opens and reads a text file named `sample.txt`.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

---

## 🎯 Objective

The objective of this program is to understand how to read data from a text file and handle file-related errors using exception handling in Python.

---

## 🛠️ Technologies Used

- Python 3.x
- File Handling
- Exception Handling

---

## 📁 File Used

```
sample.txt
```

---

## 📚 Concepts Covered

- `open()` function
- File modes
  - `rt` – Read Text Mode
- `readline()`
- `try`
- `except`
- `FileNotFoundError`
- `os.path.exists()`
- Context Manager (`with` statement)

---

## ▶️ How to Run

1. Open the project in Visual Studio Code.
2. Make sure the `sample.txt` file is present in the same folder as the Python program.
3. Open the terminal.
4. Run the program using:

```bash
python task1.py
```

5. The program reads the file line by line and displays its contents.
6. If the file does not exist, an appropriate error message is displayed.

---

## 💻 Sample Input (`sample.txt`)

```
This is a sample text file.
It contains multiple lines.
```

---

## 💻 Sample Output

```
Reading file content:

Line 1: This is a sample text file.
Line 2: It contains multiple lines.
```

### If the file does not exist

```
Error: The file 'sample.txt' was not found.
```

---

## 📖 Program Explanation

### Step 1

Import the `os` module to work with file-related operations.

### Step 2

Store the file name in a variable.

### Step 3

Use a `try` block to attempt opening the file in read mode.

### Step 4

Read the first and second lines using the `readline()` method.

### Step 5

Display the contents of the file line by line.

### Step 6

If the file is missing, the `except FileNotFoundError` block catches the exception and displays an error message instead of terminating the program.

---

## 📂 Project Structure

```
Task1/
│── task1.py
│── sample.txt
└── README.md
```

---

## ✅ Features

- Reads a text file line by line.
- Uses `readline()` for reading file content.
- Implements exception handling using `try` and `except`.
- Prevents the program from crashing when the file is not found.
- Uses the `with` statement for automatic file handling.

---

## 👨‍💻 Author

**Vivek Ananda Satpute**

Python Assignment – File Handling and Exception Handling

---