from fastapi import APIRouter, HTTPException
import logging
from dal import *
from redis_connection import search_query, cache_query

router = APIRouter()
logging.info('router created')


@router.get('/analytics/alerts-by-border-and-priority')
def alerts_by_border_and_priority():
    try:
        result = search_query(query_key='top-urgent-zones')
        if not result:
            logger.info('result is not cached')
            result = board_and_priority()
            cache_query('top-urgent-zones', result)
            logger.info('result cached')
            return result
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/analytics/top-urgent-zones')
def top_urgent_zones():
    try:
        result = search_query(query_key='top-urgent-zones')
        if not result:
            logger.info('result is not cached')
            result = five_top_zones()
            cache_query('top-urgent-zones', result)
            logger.info('result cached')
            return result
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/analytics/distance-distribution')
def distance_distribution():
    try:
        result = search_query(query_key='top-urgent-zones')
        if not result:
            logger.info('result is not cached')
            result = distribution()
            cache_query('top-urgent-zones', result)
            logger.info('result cached')
            return result
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/analytics/low-visibility-high-activity')
def low_visibility_high_activity():
    try:
        result = search_query(query_key='top-urgent-zones')
        if not result:
            logger.info('result is not cached')
            result = visibility_and_activity()
            cache_query('top-urgent-zones', result)
            logger.info('result cached')
            return result
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/analytics/hot-zones')
def hot_zones():
    try:
        result = search_query(query_key='top-urgent-zones')
        if not result:
            logger.info('result is not cached')
            result = get_hot_zones()
            cache_query('top-urgent-zones', result)
            logger.info('result cached')
            return result
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))
