import requests
from pymongo import MongoClient
from pprint import pprint

# 1 - Connect to MongoDB and Database
client = MongoClient()
db = client['nobel']

# 2 - Import the data as documents
for collection_name in ['prizes', 'laureates']:
    response = requests.get(f'http://api.nobelprize.org/v1/{collection_name[:-1]}.json')
    documents = response.json()[collection_name]
    db[collection_name].insert_many(documents)

# 3 - Accessing collections / counting documents in collection
prizes = db['prizes']
laureates = db['laureates']

len_prizes = prizes.count_documents({})
len_laureates = laureates.count_documents({})

print(f'There are {len_prizes} prizes and {len_laureates} laureates in the database.')
