from pymongo import MongoClient
import logging
from os import getenv


MONGO_COLLECTION = getenv('MONGODB_COLLECTION', 'alert')
MONGO_DATABASE = getenv('MONGODB_DATABASE', 'alert')
MONGO_URI = getenv('MONGO_URI', 'mongodb://root:password@localhost:27017/?authSource=admin')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

client = MongoClient(MONGO_URI)

def get_collection():
    db = client[MONGO_DATABASE]
    collection = db[MONGO_COLLECTION]
    return collection

