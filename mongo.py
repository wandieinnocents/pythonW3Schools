import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]


#check if the db exists

# print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
else:
    print("database does not exist.")

