from datetime import datetime
from redis_connection import get_redis_connection
from mongo_connection import save_alert
import logging
import json

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def add_timestemp(alert: dict):
    current_time = datetime.now().strftime(format="%d/%m/%Y, %H:%M:%S")
    alert["time_insertion"] = current_time
    return alert

r = get_redis_connection()

def queue_urgent_listener():
    queue_name = "queue_urgent"
    while True:
        logger.info(f'Messages waite in queue: {r.llen(name=queue_name)}')
        alert = r.brpoplpush(queue_name, 'tmp_queue')
        if not alert:
            return False
        dict_alert = json.loads(alert)
        add_timestemp(dict_alert)
        save_alert(dict_alert)
        r.lrem('tmp_queue', 1, alert)
        return True



def queue_normal_listener():
    queue_name = "queue_normal"
    while True:
        logger.info(f'Messages waite in queue: {r.llen(name=queue_name)}')
        alert = r.brpoplpush(queue_name, 'tmp_queue')
        if not alert:
            return False
        dict_alert = json.loads(alert)
        add_timestemp(dict_alert)
        save_alert(dict_alert)
        r.lrem('tmp_queue', 1, alert)
        return True



def main_listener():
    pass




new = "time_insertion"