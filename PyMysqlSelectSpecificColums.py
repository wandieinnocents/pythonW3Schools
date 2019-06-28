
#selecting specific columns from tables


import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    passwd = "wandie22",
    database = "w3schools"
)

mycursor = mydb.cursor()

#statement to select all data from table customers
mycursor.execute("SELECT name,address FROM customers ")

#fetch data from table
specific_data= mycursor.fetchall()

#iterate and fetch * all -  data from table[customers]
for table_data_values in specific_data:
    print(table_data_values)

