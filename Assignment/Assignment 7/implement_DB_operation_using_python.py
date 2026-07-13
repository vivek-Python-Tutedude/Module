import psycopg2 as p

# Function to connect to PostgreSQL
def connect_database(dbname):
    con = p.connect( dbname=dbname, user="postgres", password="vivek@2005", host="localhost", port="5433")
    return con


# Create a new database
def create_database():

    con = connect_database("postgres")
    con.autocommit = True

    cursor = con.cursor()

    dbname = input("Enter database name: ")

    cursor.execute(f"create database {dbname};")

    print("Database created successfully.")

    cursor.close()
    con.close()


# Create a table
def create_table():

    dbname = input("Enter database name: ")

    con = connect_database(dbname)
    cursor = con.cursor()

    tablename = input("Enter table name: ")

    n = int(input("Enter number of columns: "))

    query = f"create table {tablename}("

    for i in range(n):

        column = input(f"Enter column {i + 1} name: ")
        datatype = input(f"Enter datatype of {column}: ")

        query += column + " " + datatype

        if i != n - 1:
            query += ","

    query += ");"

    cursor.execute(query)
    con.commit()

    print("Table created successfully.")

    cursor.close()
    con.close()


# Insert a record
def insert_record():

    dbname = input("Enter database name: ")
    tablename = input("Enter table name: ")

    con = connect_database(dbname)
    cursor = con.cursor()

    name = input("Enter name: ")
    id = int(input("Enter id: "))
    age = int(input("Enter age: "))

    query = f"insert into {tablename}(name,id,age) values(%s,%s,%s);"

    cursor.execute(query, (name, id, age))

    con.commit()

    print("Record inserted successfully.")

    cursor.close()
    con.close()


# Fetch the first record
def fetch_one():

    dbname = input("Enter database name: ")
    tablename = input("Enter table name: ")

    con = connect_database(dbname)
    cursor = con.cursor()

    cursor.execute(f"select * from {tablename};")

    data = cursor.fetchone()

    print("\nRecord:")
    print(data)

    cursor.close()
    con.close()


# Fetch all records
def fetch_all():

    dbname = input("Enter database name: ")
    tablename = input("Enter table name: ")

    con = connect_database(dbname)
    cursor = con.cursor()

    cursor.execute(f"select * from {tablename};")

    data = cursor.fetchall()

    print("\nAll Records")

    for record in data:
        print(record)

    cursor.close()
    con.close()


# Fetch record using where condition
def select_record():

    dbname = input("Enter database name: ")
    tablename = input("Enter table name: ")

    con = connect_database(dbname)
    cursor = con.cursor()

    id = int(input("Enter id: "))

    query = f"select * from {tablename} where id = %s;"

    cursor.execute(query, (id,))

    data = cursor.fetchone()

    print("\nRecord:")
    print(data)

    cursor.close()
    con.close()


# Remove all records from the table
def truncate_table():

    dbname = input("Enter database name: ")
    tablename = input("Enter table name: ")

    con = connect_database(dbname)
    cursor = con.cursor()

    cursor.execute(f"truncate table {tablename};")

    con.commit()

    print("Table truncated successfully.")

    cursor.close()
    con.close()


# Main menu
while True:

    print("\n PostgreSQL Menu")
    print("1. Create Database")
    print("2. Create Table")
    print("3. Insert Record")
    print("4. Fetch One Record")
    print("5. Fetch All Records")
    print("6. Select Record")
    print("7. Truncate Table")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_database()

    elif choice == 2:
        create_table()

    elif choice == 3:
        insert_record()

    elif choice == 4:
        fetch_one()

    elif choice == 5:
        fetch_all()

    elif choice == 6:
        select_record()

    elif choice == 7:
        truncate_table()

    elif choice == 8:
        print("Exit")
        break

    else:
        print("Invalid choice. Please try again.")