from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()
db = client['nobel']

# Accessing Collections
prizes = db['prizes']
laureates = db['laureates']

# Using operator $in
filter_in = db.laureates.count_documents(
    {
        'diedCountry': {
            '$in': ['France', 'USA']
        }
    }
)

print(f'Number of laureates who died in France or Germany: {filter_in}')

# Using operator $ne
filter_ne = db.laureates.count_documents(
    {
        'diedCountry': {
            '$ne': 'USA'
        }
    }
)

print(f'Number of laureates who not died in USA: {filter_ne}')