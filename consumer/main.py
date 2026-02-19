from datetime import datetime
from redis_connection import get_redis_connection
from mongo_connection import save_alert
import logging
import json

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

r = get_redis_connection()

def add_timestamp(alert: dict):
    current_time = datetime.now().strftime(format="%d/%m/%Y, %H:%M:%S")
    alert["time_insertion"] = current_time
    logger.info(f'timestamp added: {current_time}')
    return alert


def queue_urgent_listener():
    queue_name = "queue_urgent"
    while True:
        try:
            logger.info(f'Messages waite in queue: {r.llen(name=queue_name)}')
            alert = r.brpoplpush(queue_name, 'tmp_queue')
            if not alert:
                return False
            dict_alert = json.loads(alert)
            add_timestamp(dict_alert)
            save_alert(dict_alert)
            r.lrem('tmp_queue', 1, alert)
            return True
        except Exception as e:
            logger.error(e)



def queue_normal_listener():
    queue_name = "queue_normal"
    while True:
        try:
            logger.info(f'Messages waite in queue: {r.llen(name=queue_name)}')
            alert = r.brpoplpush(queue_name, 'tmp_queue')
            if not alert:
                return False
            dict_alert = json.loads(alert)
            add_timestemp(dict_alert)
            save_alert(dict_alert)
            r.lrem('tmp_queue', 1, alert)
        except Exception as e:
            logger.error(e)
    return True



def main_listener():
    while True:
        logger.info('start listen to urgent queue')
        success = queue_urgent_listener()
        if not success:
            logger.info('urgent queue is empty')
            logger.info('start listen to normal queue')
            success = queue_normal_listener()
            if not success:
                logger.info('normal queue is empty')
                continue

main_listener()
