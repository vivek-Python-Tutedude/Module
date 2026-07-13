import psycopg2 as p
def table() :
    con = p.connect(dbname = "postgres", user = "postgres", password = "vivek@2005", host = "localhost", port = "5433")
    # created a connection with the data base
    print("Connected successfully")

    cursor = con.cursor()
    cursor.execute(''' create table employees(Name Text, ID int, Age int);''') # paassing the query
    print('Table created successfully')

    con.commit() # commiting the changes
    con.close()
    
def data() :
    con = p.connect(dbname = "postgres", user = "postgres", password = "vivek@2005", host = "localhost", port = "5433")
    # created a connection with the data base
    print("Connected successfully")

    cursor = con.cursor()
    cursor.execute(''' insert into  employees(Name, ID, Age) values('Vivek', 1, 21);''') # paassing the query
    print('Data Added successfully')

    con.commit() # commiting the changes
    con.close()
    
def extract() :
    con = p.connect(dbname = "postgres", user = "postgres", password = "vivek@2005", host = "localhost", port = "5433")
    # created a connection with the data base
    print("Connected successfully")

    cursor = con.cursor()
    cursor.execute(''' select * from employees;''') # paassing the query
    # print(cursor.fetchone()) # ('Vivek', 1, 21) it will fetch onyl 1st data in the form of tuple
    print(cursor.fetchall()) # it will fetch all data in the form of tuple 
    con.commit() # commiting the changes
    con.close()


"""
def extract() :
    con = p.connect(dbname = "postgres", user = "postgres", password = "vivek@2005", host = "localhost", port = "5433")
    # created a connection with the data base
    print("Connected successfully")

    cursor = con.cursor()
    cursor.execute(''' select * from employees;''') # paassing the query
    show = cursor.fetchone()
    
    print(f"Name = {show[0]}  ID = {show[1]}  Age = {show[2]}") # Name = Vivek  ID = 1  Age = 21
    # using index value of tuple we can access the individual element
    
    con.commit() # commiting the changes
    con.close()
"""
extract()
