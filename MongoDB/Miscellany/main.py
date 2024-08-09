from pymongo import MongoClient

client =  MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# Count the number of laureates who have won a prize in physics with a share of 1
print(db.laureates.count_documents({
    'prizes': {
        '$elemMatch': {
            'category': 'physics',
            'share': '1'
        }
    }
}))

# Every laureate who have prizes in physics with a share of 1 before 1945
winners_before_1945 = list(db.laureates.find({
    'prizes': {
        '$elemMatch': {
            'category': 'physics',
            'share': '1',
            'year': {'$lt': '1945'}
        }
    }
}))

# Print the first 5 winners
for winner in winners_before_1945[:5]:
    print(winner['firstname'], winner['surname'])