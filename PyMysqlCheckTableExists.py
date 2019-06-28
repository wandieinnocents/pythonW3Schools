#checking if table exists in the database

import mysql.connector


mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    passwd = "wandie22",
    database = "w3schools"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

#check existing tables in database

for tables in mycursor:
    print(tables)

#hence table exists in the database : w3schools
