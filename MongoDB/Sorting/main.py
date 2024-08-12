from pymongo import MongoClient

client =  MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# Acending order
cursor = db.prizes.find(
    {'category': 'physics'},
    ['year'],
    sort=[('year', 1)]
)

print([doc['year'] for doc in cursor][:5])

# Descending order
cursor = db.prizes.find(
    {'category': 'physics'},
    ['year'],
    sort=[('year', -1)]
)

print([doc['year'] for doc in cursor][:5])

# Prizes between 1966 and 1967
for doc in db.prizes.find(
    {'year': {'$gte': '1966', '$lt': '1968'}},
    ['category', 'year'],
    sort=[('year', 1), ('category', -1)]
):
    print([doc['year'], doc['category']])
