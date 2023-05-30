from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
print("test file")


uri = "mongodb+srv://web420_admin:aslan123@bellevueuniversity.5jww2it.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
