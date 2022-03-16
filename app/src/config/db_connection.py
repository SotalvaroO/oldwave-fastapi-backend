# MongoDB async Driver 
#import motor.motor_asyncio
# MongoDB Driver
from pymongo import MongoClient

mongo_url: str = "mongodb://localhost:27017"

#client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
client = MongoClient(mongo_url)

data_base = client.oldwave
product_collection = data_base.products
