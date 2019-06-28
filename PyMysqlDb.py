#woring with mysql database - python

#to install mysql type
#python -m pip install mysql-connector | in your terminal

#import mysql connector for database operations
import  mysql.connector


#establish a connection

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="wandie22"
)

mycursor = mydb.cursor()

#create database
#mycursor.execute("CREATE DATABASE w3schools")

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
