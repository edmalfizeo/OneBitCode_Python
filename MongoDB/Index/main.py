from pymongo import MongoClient
import timeit

client =  MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# Find prizes for the year 1910
def get_prizes():
     list(db.prizes.find({"year": "1910"}))

# Function for finding the time execution
def time_execution(function):
    execution_time = timeit.timeit(function, globals=globals(), number=1) * 1000
    print(f"Execution time: {execution_time:.2f} ms")
    
time_execution('get_prizes()')

db.prizes.create_index([("year", 1)])
time_execution('get_prizes()')

db.prizes.create_index([("year", 1), ("category", 1)])

def get_all_prizes_economics():
    list(db.prizes.find({"category": "economics"}, {"year": 1, "category": 1}))

time_execution('get_all_prizes_economics()')