from pymongo import MongoClient

client = MongoClient()

db = client.obcblog
collection = db.posts

myquery = {"title": "Automation"}

delete = collection.delete_one(myquery)

print(f"{delete.deleted_count} Document with title {myquery['title']} correctly deleted.")
