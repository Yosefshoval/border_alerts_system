import redis
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

REDIS_HOST = getenv('REDIS_HOST', 'redis')
REDIS_PORT = getenv('REDIS_PORT', 6379)


def get_redis_connection():
    r = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT), db=0)
    logger.info('redis producer created')
    return r

