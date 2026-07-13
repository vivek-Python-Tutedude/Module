import psycopg2 as p
connect = p.connect(dbname = "postgres", user = "postgres", password = "vivek@2005", host = "localhost", port = "5433")

print("Connected successfully")