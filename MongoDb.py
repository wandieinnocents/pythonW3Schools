#working with mongoDB

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mongodb_wandie"]


#print(myclient.list_database_names())

# create a collection / table -

mycol = mydb["customers"]

