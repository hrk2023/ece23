import os
from pymongo import MongoClient
# DATABASE_URI = os.environ.get('DATABASE_URI',"default_value")
cluster = MongoClient('mongodb+srv://admin:nydqqzuy1324@cluster0.oobol.mongodb.net/')
db = cluster.eceSite
cluster2 = MongoClient('mongodb+srv://admin:nydqqzuy1324@cluster0.fglir.mongodb.net/')
db2 = cluster2.ecesite
