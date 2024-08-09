from pymongo import MongoClient

client =  MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# 1 - Included Values
# 0 - Not Included Values

docs = db.laureates.find(
    filter = {},
    projection = {
        'prizes.affiliations': 1,
        '_id': 0
    }
)

for doc in docs[:3]:
    print(doc)

# Projection with Ausent Field
docs_2 = db.laureates.find(
    filter = {'gender': 'org'},
    projection = {'_id': 0, 'firstname': 1}
)

for doc in docs_2[:3]:
    print(doc)
