import json
import os

import aiohttp
from aiohttp import ClientConnectionError
from fastapi import HTTPException

from backend.database.user import get_user
from ..elastic.pollution import get_current_pollution
from ..monster_status import damage
from ..classes import RegisterJourney, JourneyUpdate, Coords, JourneyType

MAP_QUEST_URL = 'http://www.mapquestapi.com/directions/v2/route'
MAP_QUEST_KEY = os.environ['MAP_QUEST_API_KEY']


class RouteNotFoundError(BaseException):
    pass


async def get_route(start: Coords, end: Coords):
    async with aiohttp.ClientSession() as session:
        params = {'key': MAP_QUEST_KEY,
                  'from': f'{start.lat},{start.lon}',
                  'to': f'{start.lat},{end.lon}'}
        print(params)
        try:
            resp = await session.get(MAP_QUEST_URL, params=params)
            road = json.loads(await resp.text())
            dst = road['route']['distance']
            fuel = road['route']['fuelUsed']
        except KeyError:
            raise RouteNotFoundError
        return dst, fuel


async def handle_journey_register(user_id: int, journey: RegisterJourney):
    try:
        dst, fuel = await get_route(journey.start, journey.end)
    except RouteNotFoundError:
        raise HTTPException(404, 'Route not found')
    except ClientConnectionError:
        raise HTTPException(500, 'Mapquest API not responding')

    # user = get_user(user_id=user_id, include_fight=True)


    # damage_taken = damage(1, get_current_pollution())

    params = {'distance': dst,
              'fuel_saved': fuel,
              'monster_hp': 0,
              'hp': 0}
    return JourneyUpdate(**params)
