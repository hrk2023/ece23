import os
from pymongo import MongoClient
DATABASE_URI = os.environ.get('DATABASE_URI',"default_value")
DATABASE_URI_TWO = os.environ.get('DATABASE_URI_TWO',"default_value")

cluster = MongoClient(DATABASE_URI)
db = cluster.eceSite
cluster2 = MongoClient(DATABASE_URI_TWO)
db2 = cluster2.ecesite
