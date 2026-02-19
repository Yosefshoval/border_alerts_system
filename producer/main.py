from confluent_kafka import Producer
import logging
import json



logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



file_path = 'border_alerts.json'

producer_config = {

}
x = "queue_urge"
y = "queue_normal"

new_field = "priority" ('URGENT', 'NORMAL')

producer = Producer(producer_config)
logger.info('producer created')


def open_file():
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data



