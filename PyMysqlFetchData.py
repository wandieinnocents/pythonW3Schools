#fecth data from the database

import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    passwd = "wandie22",
    database = "w3schools"
)

mycursor = mydb.cursor()

#statement to select all data from table customers
mycursor.execute("SELECT * FROM customers")

#fetch data from table
data = mycursor.fetchall()

#iterate and fetch * all -  data from table[customers]
for table_customer_values in data:
    print(table_customer_values)

