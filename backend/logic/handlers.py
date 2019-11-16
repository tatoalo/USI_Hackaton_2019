import json
import os

import aiohttp
from aiohttp import ClientConnectionError
from fastapi import HTTPException

from backend.database.user import get_user, update_user_stats, update_user_fight
from ..elastic.pollution import get_current_pollution
from ..monster_status import damage
from ..classes import RegisterJourney, JourneyUpdate, Coords, JourneyType, User

MAP_QUEST_URL = 'http://www.mapquestapi.com/directions/v2/route'
MAP_QUEST_KEY = os.environ['MAP_QUEST_API_KEY']


class RouteNotFoundError(BaseException):
    pass


def get_monster_damage(dst, fuel, type, pollution):
    monster_damage = damage(1, pollution)

    if type == JourneyType.bus:
        monster_damage = int(monster_damage * 0.8)
    elif type == JourneyType.car:
        monster_damage = 0

    return monster_damage


def get_user_damage(dst, fuel, type, pollution):
    user_damage = 0
    if type == JourneyType.bus:
        user_damage = int(fuel+3)
    elif type == JourneyType.car:
        user_damage = int((fuel+3)*5)
    return user_damage

def update_user(user: User, monster_damage, user_damage):
    new_xp = ...#

    await update_user_stats(
        user_id=user.id,
        hp=user.hp - user_damage,
        xp=new_xp,
        level=new_level,
        xp_required=new_xp_required)
    await update_user_fight(
        user_id=user.id,
        monster_hp=new_monster_hp)
    return new_monster_hp


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

    pollution = get_current_pollution()
    user = get_user(user_id=user_id)
    monster_damage = get_monster_damage(dst, fuel, journey.type, pollution)
    user_damage = get_user_damage(dst, fuel, journey.type, pollution)

    update_user(user, monster_damage, user_damage)

    params = {'distance': dst,
              'fuel_saved': fuel,
              'monster_hp': 0,
              'hp': 0}
    return JourneyUpdate(**params)
