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
    
data()