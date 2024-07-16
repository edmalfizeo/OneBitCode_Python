from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

db = client.obcblog
collection = db.posts

old_post = {"content": "data is the new oil"}
new_post = {"$set": {"content": "data analysis is super important"}}

collection.update_one(old_post, new_post)
print('Document correctly updated.')

for post in collection.find():
    pprint(post)
    print('\n')