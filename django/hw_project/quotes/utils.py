from pymongo import MongoClient

def get_mongodb():
    client = MongoClient("mongodb://localhost:27023")
    db = client.hw
    return db
