from mongo_connection import get_collection
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def board_and_priority():
    cursor = get_collection()
    result = cursor.aggregate([
        {},
        {}
    ])

    dict_result = result.to_list()
    return dict_result


def five_top_zones():
    cursor = get_collection()
    result = cursor.aggregate([
        {
            "$match": {"priority": "URGENT"}
        },
        {
            "$group": {
                "_id" : "$zone",
                "alerts_count" : {"$sum" : 1}
            }
        },
        {
            "$sort": {"alerts_count": -1}
        },
        { "$limit": 5 }

    ])

    dict_result = result.to_list()
    return dict_result


def distribution():
    cursor = get_collection()
    result = cursor.aggregate([
        {},
        {}
    ])

    dict_result = result.to_list()
    return dict_result


def visibility_and_activity():
    cursor = get_collection()
    result = cursor.aggregate([
        {},
        {}
    ])

    dict_result = result.to_list()
    return dict_result


def get_hot_zones():
    cursor = get_collection()
    result = cursor.aggregate([
        {},
        {}
    ])

    dict_result = result.to_list()
    return dict_result
