
#insert data in table in python table

import mysql.connector


mydb = mysql.connector.connect(

    host="localhost",
    user = "root",
    passwd = "wandie22",
    database = "w3schools"

)


mycursor = mydb.cursor()

#creating sql statements to save data to table

sql =  "INSERT INTO customers(name,address,contact) values (%s ,%s,%s) "
val = ("Wandie Innocent","Kampala, Uganda", "0706382817")

#exectute the statement
mycursor.execute(sql,val)

#submit the data to the database
mydb.commit()
print(mycursor.rowcount(),"Record Inserted")



