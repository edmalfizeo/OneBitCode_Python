from pymongo import MongoClient

client = MongoClient()
db = client.obcblog
collection = db.posts

post1 = {
    'title': 'Automation',
    'content': 'automation is the future',
    'author': {
        'name': 'Lucas',
        'email': 'lucas@gmail.com'
    }
}

cursor = collection.insert_one(post1)
print('Document correctly inserted.')

