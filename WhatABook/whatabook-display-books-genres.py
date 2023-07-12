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
selectedGenre = input("Please enter genre: ")
print(selectedGenre)
if selectedGenre != "":
    print("----------Display books by genre------")
    for x in db.books.find({"genre": selectedGenre}):
        print(x)
# not completed yet
for x in db.books.aggregate({ $lookup: { genre: "genre"}}):
    print(x)
