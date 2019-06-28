#alter table and add primary key to a colum in the table : database

import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    passwd = "wandie22",
    database = "w3schools"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#successfuly added id to table customers