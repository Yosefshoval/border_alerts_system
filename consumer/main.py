from datetime import datetime
from redis_connection import get_redis_connection
from mongo_connection import save_alert
import logging
import json
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

r = get_redis_connection()
logger.info('redis connection created')


def add_timestamp(alert: dict):
    current_time = datetime.now().strftime(format="%d/%m/%Y, %H:%M:%S")
    alert["time_insertion"] = current_time
    logger.info(f'timestamp added: {current_time}')
    return alert



def listener(queue_name: str):
    while True:
        time.sleep(0.5)
        try:
            logger.info(f'Messages waite in queue {queue_name}: {r.llen(name=queue_name)}')
            if r.llen(name=queue_name) == 0:
                return False
            alert = r.brpoplpush(queue_name, f'tmp_{queue_name}')
            if not alert:
                return False
            dict_alert = json.loads(alert)
            add_timestamp(dict_alert)
            save_alert(dict_alert)
            r.lrem('tmp_queue', 1, alert)
        except Exception as e:
            logger.error(e)
    return True



def main_listener():
    while True:
        logger.info('start listen to urgent queue')
        success = listener('queue_urge')
        if not success:
            logger.info('urgent queue is empty')
            logger.info('start listen to normal queue')
            success = listener('queue_normal')
            if not success:
                logger.info('normal queue is empty')
                continue

main_listener()
