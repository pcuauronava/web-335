# ==========================
# Title: cuauro_usersp1.py
# Author: Richard Krasso
# Modified by: Patrick Cuauro
# Date: Jun 29 2023
# Description: Exercise 6.3
# ==========================

from pymongo import MongoClient

# Connection string to connect to database
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@bellevueuniversity.5jww2it.mongodb.net/?retryWrites=true&w=majority")
# specify the database to connect
db = client["web335DB"]
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print(client)
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("List of all documents in the users collection")
print("-----------------------------------------------------------")
# display a list of all documents in the users collection
for user in db.users.find():
    print("")
    print(user)
print("-----------------------------------------------------------")
print("Printing employeeId 1011")
# Shows the document where the employeeId is 1011
print("-----------------------------------------------------------")
print(db.users.find_one({"employeeId": "1011"}))
print("-----------------------------------------------------------")
print("Document with lastName Mozart")
# Shows the document with the lastName Mozart
print("-----------------------------------------------------------")
print(db.users.find_one({"lastName": "Mozart"}))
