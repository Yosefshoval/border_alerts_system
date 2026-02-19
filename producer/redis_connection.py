""" redis """
import redis
from os import getenv
import logging
import json
from datetime import datetime

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

TTL = 20

REDIS_HOST = getenv('REDIS_HOST', 'redis')
REDIS_PORT = getenv('REDIS_PORT', 6379)

r = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT), db=0)

logger.info('redis producer created')

urge = "queue_urge"
normal = "queue_normal"


def push_alert(alert: dict):
    if alert.get("_id"): alert["_id"] = str(alert["_id"])
    if alert.get('timestamp'): alert['timestamp'] = str(alert['timestamp'])

    queue = urge if alert['priority'] == 'URGENT' else normal
    r.lpush(
        queue,
        json.dumps(alert)
    )
    logger.info(f'alert {alert["border"]} pushed to queue {queue}')
    logger.info(f'queue {queue} now has {r.llen("queue_orders")} alerts.')
    return True
