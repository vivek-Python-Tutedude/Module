# PostgreSQL Database Operations Using Python

## Project Overview

This project demonstrates how to perform basic PostgreSQL database operations using Python and the `psycopg2` library. It is a menu-driven application that allows the user to create databases, create tables, insert records, fetch records, search records, and truncate tables.

---

## Features

- Connect to PostgreSQL
- Create a new database
- Create a table with user-defined columns
- Insert records using parameterized queries
- Fetch the first record
- Fetch all records
- Search records using a WHERE condition
- Truncate a table
- Menu-driven interface

---

## Technologies Used

- Python 3.13.x
- PostgreSQL
- psycopg2
- VS Code

---

## Project Structure

```
DatabaseOperations-YourName/
│
├── implement_DB_operation_using_python.py
├── README.md
├── Screenshots/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   ├── 6.png
│   ├── 7.png
│   └── 8.png
```

---

## Requirements

- Python 3.13.x
- PostgreSQL Server
- psycopg2 library

Install psycopg2 using:

```
bash
pip install psycopg2
```

or

```
bash
pip install psycopg2-binary
```

---

## Database Connection

Update the connection details in the program if required.

```
python
dbname="postgres"
user="postgres"
password="your_password"
host="localhost"
port="5433"
```

---

## How to Run

1. Start the PostgreSQL server.
2. Open the project in VS Code.
3. Activate the virtual environment (if used).
4. Run the program.

```
bash
python implement_DB_operation_using_python.py
```

---

## Menu

```
1. Create Database
2. Create Table
3. Insert Record
4. Fetch One Record
5. Fetch All Records
6. Select Record
7. Truncate Table
8. Exit
```

---

## Operations Performed

### Create Database
Creates a new PostgreSQL database.

### Create Table
Creates a table with user-defined columns and data types.

### Insert Record
Inserts records into the selected table using parameterized queries.

### Fetch One Record
Displays the first record from the table.

### Fetch All Records
Displays all records present in the table.

### Select Record
Retrieves a record based on the entered ID using a WHERE condition.

### Truncate Table
Removes all records from the selected table while keeping the table structure.

---

## Sample Output

```
PostgreSQL Menu

1. Create Database
2. Create Table
3. Insert Record
4. Fetch One Record
5. Fetch All Records
6. Select Record
7. Truncate Table
8. Exit
```

---

## Learning Outcomes

- Connecting Python with PostgreSQL
- Executing SQL queries using psycopg2
- Creating databases and tables
- Using parameterized queries
- Fetching records with fetchone() and fetchall()
- Using SELECT with WHERE
- Truncating tables
- Working with transactions using commit()

---

## Author

**Name:** Vivek Ananda Satpute

---

