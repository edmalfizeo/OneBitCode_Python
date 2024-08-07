from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()
db = client['nobel']

# Accessing Collections
prizes = db['prizes']
laureates = db['laureates']

qtd = db.laureates.count_documents({})
print(f'Total of laureates: {qtd}')

# Verify if prize is not empty
prizes_contain = db.laureates.count_documents({'prizes.0': {'$exists': True}})
print(f'Number of laureates who win the Nobel Prize: {prizes_contain}')

# Searching for laureates who win more than one Nobel Prize
winners = db.laureates.count_documents({
    'prizes.1': {'$exists': True}
})
print(f'Number of laureates who win more than one Nobel Prize: {winners}')
