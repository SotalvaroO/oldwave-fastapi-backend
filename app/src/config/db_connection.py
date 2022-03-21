# MongoDB async Driver 
#import motor.motor_asyncio
# MongoDB Driver
from pymongo import MongoClient
import os

mongo_url: str = "mongodb://localhost:27017"
mongo_atlas_url: str = os.environ['MONGO_URL']
#mongo_atlas_url: str = "mongodb+srv://DirtyDann:Seattle3317@databasecluster.1ry5d.mongodb.net/test"

#client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
client = MongoClient(mongo_atlas_url)

data_base = client.oldwave
product_collection = data_base.products
