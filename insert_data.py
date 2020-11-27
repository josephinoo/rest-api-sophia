import json
import pymongo
from search_engine.main import *
from bson.json_util import dumps
client = pymongo.MongoClient("localhost", 27017)
db = client.sophia
collection = db.queries
"""
query = "Sea"
results = query_search(query)
insertDa = {"query": query, "results": results}
insertDB = collection.insert_one(insertDa)
"""

file_keywords = open("search_engine/keywords.txt", "r")
for query in file_keywords:
    results = query_search(query.strip())
    insertDa = {"query": query.strip(), "results": results}
    insertDB = collection.insert_one(insertDa)

"""
curson = collection.find({"query": "Earth observation"})
list_cur = list(curson)


json_data = dumps(list_cur, indent=2)

with open('data.json', 'w') as file:
    file.write(json_data)"""
