# MongoDB Driver async
import motor.motor_asyncio

mongo_url: str = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)

data_base = client.oldwave
product_collection = data_base.products
