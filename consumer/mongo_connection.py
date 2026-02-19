from pymongo import MongoClient
import logging

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

