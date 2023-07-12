# ==========================
# Title: Fighting-Lions-Whatabook.py
# Author: Richard Krasso
# Modified by: Patrick Cuauro
# Date: Jul 09 2023
# Description: Whatabook Part 1
# scripts for MongoDB operations
# ==========================

from pymongo import MongoClient
# this is to automatically add the date to the document insertion
# import datetime

# Connection string to connect to database
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@bellevueuniversity.5jww2it.mongodb.net/?retryWrites=true&w=majority")
# specify the database to connect
db = client["Whatabook"]
print("-----------------------------------------------------------")
print("----------client Whatabook---------------------------------")
print(client)
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
db = client["Whatabook"]
print("----------client-------------------------------------------")
print(client)

collection = db["books"]

# 1. Display a list of books.
# 2. Display a list of books by genre.
# 3. Display a list of books by author.
# 4. Display a book by bookId.
# 5. Display a wishlist by customerId.
# 6. Add books to a customer’s wishlist.
# 7. Remove book from a customer’s wishlist.
# predetermined book, with title, genre, author
# book = {
#     "bookId": 1100,
#     "title": "The Lord Of The Rings: The Return Of The King",
#     "genre": "fantasy",
#     "author": "J.R.R. Tolkien"
# }
# predetermined customer, with customerId, firstName, lastName
# customer = {
#     "customerId": "c00001",
#     "firstName": "Patrick",
#     "lastName": "Cuauro",
# }
# 1. Display a list of books.
print("----------Display books------------------------------------")
for x in db.books.find():
    print(x)
# 2. Display a list of books by genre.
selectedGenre = input("Please enter genre: ")
if selectedGenre != "":
    print("----------Display books by genre------")
    for x in db.books.find({"genre": selectedGenre}):
        print(x)
