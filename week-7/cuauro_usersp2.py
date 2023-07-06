# ==========================
# Title: cuauro_usersp2.py
# Author: Richard Krasso
# Modified by: Patrick Cuauro
# Date: Jul 05 2023
# Description: Exercise 7.3
# scripts for MongoDB operations
# ==========================

from pymongo import MongoClient
# this is to automatically add the date to the document insertion
import datetime

# Connection string to connect to database
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@bellevueuniversity.5jww2it.mongodb.net/?retryWrites=true&w=majority")
# specify the database to connect
db = client["web335DB"]
print("-----------------------------------------------------------")
print("----------client web335DB----------------------------------")
print(client)
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
db = client["web335DB"]
print("----------client-------------------------------------------")
print(client)

# declare the name of the user to insert
patrick = {
    "firstName": "Patrick",
    "lastName": "Cuauro",
    "employeeId": "9999",
    "email": "patrickcuauro@gmail.com",
    "datecreated": datetime.datetime.utcnow()
}

# called the function to insert the user
patrick_user_id = db.users.insert_one(patrick).inserted_id
print("----------Insert-------------------------------------------")
print(patrick_user_id)

# show the results from the insertion
print("----------Results of insert--------------------------------")
print(db.users.find_one({"employeeId": "9999"}))

# update the email for the newly created user to
# college email
print("----------Update-------------------------------------------")

db.users.update_one(
    {"employeeId": "9999"},
    {
        "$set": {
            "email": "pcuauronava@my365.bellevue.com"
        }
    }
)

# show the results for the update
print("----------Result of update---------------------------------")
print(db.users.find_one({"employeeId": "9999"}))

# delete the newly created user by id
result = db.users.delete_one({
    "employeeId": "9999"
})
# show the result of the deletion
print("----------Result of deletion-------------------------------")
print(result)

# confirmation of the user deletion
print("----------Confirmation of deletion-------------------------")
print(db.users.find_one({"employeeId": "9999"}))
