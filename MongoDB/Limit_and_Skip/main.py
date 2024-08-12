from pymongo import MongoClient
import timeit

client =  MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# Every price shared with 3 laureates
for doc in db.prizes.find({"laureates.share": '3'}):
    print([doc['year'], doc['category'], doc['laureates'][0]['firstname'], doc['laureates'][1]['firstname'], doc['laureates'][2]['firstname']])

print('\n')

# Using limit
for doc in db.prizes.find({"laureates.share": '3'}).limit(5):
    print([doc['year'], doc['category'], doc['laureates'][0]['firstname'], doc['laureates'][1]['firstname'], doc['laureates'][2]['firstname']])

print('\n')

# Using skip
for doc in db.prizes.find({"laureates.share": '3'}).skip(5):
    print([doc['year'], doc['category'], doc['laureates'][0]['firstname'], doc['laureates'][1]['firstname'], doc['laureates'][2]['firstname']])

print('\n')

# Refactoring / Using limit and skip
for doc in db.prizes.find({"laureates.share": '3'}).sort([('year', 1)]).limit(3).skip(3):
    print([doc['year'], doc['category'], doc['laureates'][0]['firstname'], doc['laureates'][1]['firstname'], doc['laureates'][2]['firstname']])
