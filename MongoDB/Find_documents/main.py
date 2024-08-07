from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()
db = client['nobel']

# Accessing Collections
prizes = db['prizes']
laureates = db['laureates']

# Count documents by gender
women_winners = db.laureates.count_documents({'gender': 'female'})
male_winners = db.laureates.count_documents({'gender': 'male'})

# Count documents by died country
died_in_france = db.laureates.count_documents({'diedCountry': 'France'})

print(f'Number of laureates who died in France: {died_in_france}')

# Composite filter with some information
filter_doc = {
    'diedCountry': 'France',
    'gender' : 'female',
    'bornCity': 'Warsaw'
}

print(db.laureates.count_documents(filter_doc))
print(db.laureates.find_one(filter_doc))