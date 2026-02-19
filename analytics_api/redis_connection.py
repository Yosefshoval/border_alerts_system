import redis
import logging
from os import getenv
import json

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

REDIS_HOST = getenv('REDIS_HOST', 'redis')
REDIS_PORT = getenv('REDIS_PORT', 6379)

TTL = 20

r = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT), db=0)
logger.info('redis producer created')


def search_query(query_key: str):
    result = r.get(name=query_key)
    return result


def cache_query(query_key: str, query_result: dict | list):
    r.set(
        name=query_key,
        value=json.dumps(query_result),
        ex=TTL
          )

