import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def determine_priority(alert: dict):
    if (alert['weapons_count'] > 0
        or alert['distance_from_fence_m'] <= 50
        or alert['people_count'] >= 8
        or alert['vehicle_type'] == "truck"):
        alert['priority'] = "URGENT"
    elif ((alert['distance_from_fence_m'] <= 150
          or alert['people_count'] >= 4)
          or (alert['vehicle_type'] == "jeep"
            or alert['people_count'] >= 3)
    ):
        alert['priority'] = "URGENT"
    else:
        alert['priority'] = "NORMAL"
    logger.info(f'priority determined: {alert}')
    return alert

