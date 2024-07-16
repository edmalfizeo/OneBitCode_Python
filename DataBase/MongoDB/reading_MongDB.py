from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

db = client.obcblog
collection = db.posts

cursor = collection.find()
for post in cursor:
    pprint(post)
    print('\n')
