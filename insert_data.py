import json
from pymongo import MongoClient
from search_engine.main import *
from bson.json_util import dumps
from dns import resolver
client = MongoClient(
    "mongodb://admin:hgr4BvOeOME9R852@cluster0-shard-00-00.qmxmg.mongodb.net:27017,cluster0-shard-00-01.qmxmg.mongodb.net:27017,cluster0-shard-00-02.qmxmg.mongodb.net:27017/sophia?ssl=true&replicaSet=atlas-vb7337-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database("sophia")
