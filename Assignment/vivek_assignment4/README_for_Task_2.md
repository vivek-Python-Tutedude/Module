# 📂 Task 2 - File Handling in Python

## 📌 Problem Statement

Write a Python program that:

1. Takes user input and writes it to a file named `sample1.txt`.
2. Appends additional user input to the same file.
3. Reads and displays the final content of the file.

---

## 🎯 Objective

The objective of this program is to understand the basic file handling operations in Python, including:

- Writing data to a file
- Appending data to an existing file
- Reading data from a file
- Using Python's `with open()` statement for automatic file management

---

## 🛠️ Technologies Used

- Python 3.x
- File Handling

---

## 📁 File Used

```
sample1.txt
```

---

## 📚 Concepts Covered

- `open()` function
- File modes:
  - `wt` – Write Text Mode
  - `at` – Append Text Mode
  - `rt` – Read Text Mode
- `input()` function
- `write()`
- `readline()`
- `read()`
- `print()`
- Context Manager (`with` statement)

---

## ▶️ How to Run

1. Open the project in Visual Studio Code.
2. Open the terminal.
3. Run the program using:

```bash
python Task2.py
```

4. Enter the required text when prompted.
5. The program will create/update `sample1.txt`.
6. The final content of the file will be displayed on the screen.

---

## 💻 Sample Output

```
Enter text to write to file:
Hello, Python!

Data successfully written to sample1.txt.

Enter text to append to file:
Learning file handling in Python.

Data successfully append.

Final content of sample1.txt.

Hello, Python!
Learning file handling in Python.
```

---

## 📖 Program Explanation

### Step 1
The program creates a file named `sample1.txt` (or overwrites it if it already exists).

### Step 2
It accepts input from the user and writes the data into the file.

### Step 3
The file is opened again in append mode to add more text without removing the existing content.

### Step 4
The program opens the file in read mode.

### Step 5
It reads the first line using `readline()` and the remaining content using `read()`.

### Step 6
Finally, it displays the complete contents of the file.

---

## 📂 Project Structure

```
Task2/
│── Task2.py
│── sample1.txt
└── README.md
```

---

## ✅ Expected Output

The program successfully:

- Creates a text file.
- Writes user input to the file.
- Appends additional data.
- Reads and displays the final file content.

---

## 👨‍💻 Author

**Vivek Ananda Satpute**

Python Assignment – File Handling

---