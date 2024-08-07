from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()
db = client['nobel']

# Accessing Collections
prizes = db['prizes']
laureates = db['laureates']

# Searching the first document
walter = db.laureates.find_one({'firstname': 'Walter', 'surname': 'Kohn'})
first_name = walter['firstname']
surname = walter['surname']
born = walter['born']
died = walter['died']
print(f'{first_name} {surname} was born in {born} and died in {died}')

# Searching on substructure
california = db.laureates.count_documents({
    'prizes.affiliations.name': 'University of California'
})
print(f'Number of laureates who have affiliation with University of California: {california}')

san_francisco = db.laureates.count_documents({
    'prizes.affiliations.city': 'San Francisco, CA'
})

print(f'Number of laureates who have affiliation with San Francisco: {san_francisco}')

# Count documents that does not have a information
no_born = db.laureates.count_documents({
    'bornCountry': {'$exists': False}
})

print(f'Number of laureates who does not have a born country information: {no_born}')