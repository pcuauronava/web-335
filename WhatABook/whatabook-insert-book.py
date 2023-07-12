from pymongo import MongoClient

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

print("-----------------------------------------------------------")
x = input("Please enter bookId: ")
y = input("Please enter title: ")
z = input("Please enter genre: ")
w = input("Please enter author: ")


def insert(x, y, z, w):
    book = {
        "bookId": x,
        "title": y,
        "genre": z,
        "author": w,
    }
    return collection.insert_one(book)


# if choice == "1":
result = insert(x, y, z, w)
print("Book inserted with id", result.inserted_id)
