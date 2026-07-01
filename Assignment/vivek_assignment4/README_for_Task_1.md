# 📂 Task 1 - Read a File and Handle Errors

## 📌 Problem Statement

Write a Python program that:

1. Opens and reads a text file named `sample.txt`.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

---

## 🎯 Objective

The objective of this program is to learn basic file handling and exception handling in Python by reading a text file and displaying an appropriate error message when the file is not found.

---

## 🛠️ Technologies Used

- Python 3.x
- File Handling
- Exception Handling

---

## 📁 Files Used

```
sample.txt
sample3.txt
task1.py
README.md
```

---

## 📚 Concepts Covered

- `open()` function
- File Modes (`rt`)
- `readline()`
- `try` and `except`
- `FileNotFoundError`
- Context Manager (`with` statement)

---

## ▶️ How to Run

1. Open the project in Visual Studio Code.
2. Place `sample.txt` in the same folder as `task1.py`.
3. Run the program using:

```bash
python task1.py
```

4. The program will:
   - Read and display the contents of `sample.txt`.
   - Attempt to open `sample3.txt`.
   - Display an error message if `sample3.txt` does not exist.

---

## 💻 Sample Input (`sample.txt`)

```
This is a sample text file.
It contains multiple lines.
```

---

## 💻 Sample Output

```
If sample.txt file exist

Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.

If sample3.txt file does not exist

Error: The file 'sample3.txt' was not found.
```

---

## 📖 Program Explanation

### Case 1: File Exists

- Opens `sample.txt` in read mode.
- Reads the first two lines using `readline()`.
- Displays the file contents.

### Case 2: File Does Not Exist

- Attempts to open `sample3.txt`.
- Since the file is missing, `FileNotFoundError` is raised.
- The `except` block catches the error and prints an appropriate message.

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
- Demonstrates the use of `readline()`.
- Uses `try` and `except` for exception handling.
- Prevents the program from crashing when a file is missing.
- Uses the `with` statement for automatic file handling.

---

## 👨‍💻 Author

**Vivek Ananda Satpute**

Python Assignment – File Handling and Exception Handling