#checking database if exists
#if no error returned then databse exists

import mysql.connector



mydb = mysql.connector.connect(

    host="localhost",
    user = "root",
    password = "wandie22",
    database = "w3schools"


)

#conditonal check if databse exists

if(mydb):
    print("Database exists in the os")
else:
    #if database does not exist
    print("Sorry: check credentials , database unknown")
