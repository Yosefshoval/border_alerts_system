from confluent_kafka import Producer
import logging
import json
from priority_logic import determine_priority
from redis_connection import push_alert


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



file_path = 'border_alerts.json'

producer_config = {

}

producer = Producer(producer_config)
logger.info('producer created')


def open_file():
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data



def main():
    try:
        data = open_file()
        if not data:
            raise Exception('not data found')

        for alert in data:
            updated_alert = determine_priority(alert=alert)
            logger.info(f'updated_alert: {updated_alert}')
            pushed = push_alert(updated_alert)
            logger.info('alert pushed successfully.')

    except Exception as e:
        logger.error(e)