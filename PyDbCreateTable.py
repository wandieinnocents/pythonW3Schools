#creating table in python database

import mysql.connector

#connect the database
mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    passwd = "wandie22",
    database = "w3schools"
)

#check if database exists

mycursor = mydb.cursor()

#create table customers with fields, 1- name: 2- address : 3- contact
mycursor.execute("CREATE TABLE customers (name VARCHAR(255) , address VARCHAR(255) , contact VARCHAR(255)) ")




