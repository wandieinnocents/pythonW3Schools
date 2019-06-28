#inserting multiple values to the table

import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    passwd = "wandie22",
    database = "w3schools"
)

mycursor = mydb.cursor()

#write statement to save data to multiple tables

#sql statement
sql = "INSERT INTO customers(name,address,contact) VALUES (%s, %s, %s)"

#values to be inserted : multiple values
#array of values


val = [

    ('User 1', 'Address 1', '0706382817'),
    ('User 2', 'Address 2', '0706382817'),
    ('User 3', 'Address 3', '0706382817'),
    ('User 4' , 'Address 5', '0706382817')

]

#submit data the database
mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount,"was inserted")


