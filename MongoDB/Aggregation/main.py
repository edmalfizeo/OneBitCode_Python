from pymongo import MongoClient
import timeit
from collections import OrderedDict

client =  MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

cursor = db.laureates.find(
    filter = {"bornCountry": "USA"},
    projection = {"firstname": 1, "surname": 1, "_id": 0},
    limit = 3
)

for doc in cursor:
    print(f'{doc['firstname'], doc['surname']} was born in the USA')

print('\n')

# Sorting search with aggregation
cursor = db.laureates.aggregate([
    {"$match": {"bornCountry": "USA"}},
    {"$project": {"firstname": 1, "surname": 1, "_id": 0}},
    {"$limit": 3},
    {"$sort": OrderedDict([("surname", 1)])}
])

for doc in cursor:
    print(f'{doc['firstname'], doc['surname']} was born in the USA')

print('\n')
