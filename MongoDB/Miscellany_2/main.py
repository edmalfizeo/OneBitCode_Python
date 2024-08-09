from pymongo import MongoClient

client =  MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# Using regex 
print(db.laureates.distinct('bornCountry', {'bornCountry': {'$regex': 'Poland'}}))

# Case insensitive (poland, Poland, POLAND)
print(db.laureates.distinct('bornCountry', {'bornCountry': {'$regex': 'poland', '$options': 'i'}}))

# Using Class Regex
from bson.regex import Regex

print(db.laureates.distinct('bornCountry', {'bornCountry': Regex('poland', 'i')}))

# Start with
print(db.laureates.distinct('bornCountry', {'bornCountry': {'$regex': '^P'}}))

# End with
print(db.laureates.distinct('bornCountry', {'bornCountry': {'$regex': 'land$'}}))
