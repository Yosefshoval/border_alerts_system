from pymongo import MongoClient
import logging
from os import getenv


MONGODB_COLLECTION = getenv('MONGODB_COLLECTION', 'pizza_orders')
MONGODB_DATABASE = getenv('MONGODB_DATABASE', 'pizza_orders')
MONGO_URI = getenv('MONGO_URI', 'mongodb://root:password@localhost:27017/?authSource=admin')


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

client = MongoClient()

def get_collection():
    db = client[MONGO_DATABASE]
    collection = db[MONGO_COLLECTION]
    return collection


def save_alert(alert: dict):
    cursor = get_collection()

    result = cursor.insert_one(
        document=alert
    )
    new_id = result.inserted_id
    logger.info(f'alert inserted. new id: {new_id}')
    return new_id

