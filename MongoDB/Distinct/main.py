from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()
db = client['nobel']

# Accessing Collections
prizes = db['prizes']
laureates = db['laureates']

# Find distinct values gender
print(f'List of genders: {db.laureates.distinct('gender')}')
print(f'Number of winners that are Org: {db.laureates.count_documents({'gender': 'org'})}')
print(f'Number of winners that are Man: {db.laureates.count_documents({'gender': 'male'})}')
print(f'Number of winners that are Women: {db.laureates.count_documents({'gender': 'female'})}')

# List map of price categories
print(f'List of categories: {db.prizes.distinct("category")}')
print(f'Number of prizes in Literature: {db.prizes.count_documents({"category": "literature"})}')
print(f'Number of prizes in Peace: {db.prizes.count_documents({"category": "peace"})}')
print(f'Number of prizes in Chemistry: {db.prizes.count_documents({"category": "chemistry"})}')
print(f'Number of prizes in Physics: {db.prizes.count_documents({"category": "physics"})}')
print(f'Number of prizes in Medicine: {db.prizes.count_documents({"category": "medicine"})}')
print(f'Number of prizes in Economics: {db.prizes.count_documents({"category": "economics"})}')

# focusing on categories besides Physics that have laureates with quarterly awards
print(f'Number of laureates with quarterly awards {db.laureates.distinct("prizes.category", {"prizes.share": "4"})}')

# Laureates with multiple awards
print(f'Number of laureates with multiple awards {db.laureates.distinct('prizes.category', {'prizes.1': {'$exists': True}})}')



