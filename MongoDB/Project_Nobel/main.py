import requests
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()

# Connect to the database called 'nobel'
db = client['nobel']

# Import data on documents
for collection_name in ["prizes", "laureates"]:
    response = requests.get(f'http://api.nobelprize.org/v1/{collection_name[:-1]}.json')
    
    documents = response.json()[collection_name]
    db[collection_name].insert_many(documents)


# Acessing Collections
prizes = db['prizes']
laureates = db['laureates']

# Get the count of prizes and laureates
prizes_count = prizes.count_documents({})
laureates_count = laureates.count_documents({})

print(f'Total number of prizes: {prizes_count}')
print(f'Total number of laureates: {laureates_count}')