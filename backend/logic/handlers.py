import asyncio
import os
from typing import Tuple

import aiohttp
from backend.database.user import (create_new_user_fight, get_user,
                                   update_user_fight, update_user_stats)

from ..classes import JourneyType, JourneyUpdate, RegisterJourney, User
from ..database.monster import get_all_monsters, get_monster
from ..elastic.pollution import get_current_pollution
from ..exceptions import RouteNotFoundError
from ..monster_status import (choose_monster, damage, obtain_xp,
                              update_xp_required)

MAP_QUEST_URL = "http://www.mapquestapi.com/directions/v2/route"
MAP_QUEST_KEY = os.environ["MAP_QUEST_API_KEY"]


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
        user_damage = int(fuel + 3)
    elif type == JourneyType.car:
        user_damage = int((fuel + 3) * 5)
    return user_damage


async def update_user(user: User, monster_damage, user_damage):
    stats, fight = user.stats, user.current_fight
    new_level = stats.lvl
    new_xp = stats.xp
    new_xp_required = stats.xp_required

    if fight.monster_hp - monster_damage <= 0:
        monsters = await get_all_monsters()
        monster = choose_monster(monsters, user.stats.lvl)
        new_xp = stats.xp + obtain_xp(await get_monster(monster_id=fight.monster_id))
        while new_xp >= new_xp_required:
            new_xp -= new_xp_required
            new_level += 1
            stats.lvl = new_level
            new_xp_required = update_xp_required(stats)
        await create_new_user_fight(user_id=user.id, monster=monster)
    else:
        await update_user_fight(user_id=user.id, new_monster_hp=fight.monster_hp - monster_damage)

    new_hp = stats.hp - user_damage if stats.lvl == new_level else 100
    if new_hp <= 0:
        new_hp = 100
        stats.lvl -= 5
        new_xp = 0
        new_xp_required = update_xp_required(stats)
        new_level = stats.lvl - 5 if stats.lvl - 5 > 1 else 1

    await update_user_stats(user_id=user.id, hp=new_hp, xp=new_xp, level=new_level, xp_required=new_xp_required)
    return new_hp


async def get_route(journey: RegisterJourney) -> Tuple[float, float]:
    async with aiohttp.ClientSession() as session:
        parameters = {
            "key": MAP_QUEST_KEY,
            "from": f"{journey.lat_start},{journey.lon_start}",
            "to": f"{journey.lat_end},{journey.lon_end}",
        }
        async with session.get(MAP_QUEST_URL, params=parameters) as response:
            try:
                road = await response.json()
                distance = road["route"]["distance"]
                fuel = road["route"]["fuelUsed"]
            except KeyError:
                raise RouteNotFoundError
        return distance, fuel


async def handle_journey_register(user_id: int, journey: RegisterJourney):
    get_route_task = asyncio.create_task(get_route(journey))
    pollution = get_current_pollution()
    user = await get_user(user_id=user_id)

    await get_route_task
    distance, fuel = get_route_task.result()

    monster_damage = get_monster_damage(distance, fuel, journey.type, pollution)
    user_damage = get_user_damage(distance, fuel, journey.type, pollution)

    await update_user(user, monster_damage, user_damage)

    new_usr = await get_user(user_id=user_id)
    params = {"user": new_usr, "distance": distance, "fuel_saved": fuel}
    return JourneyUpdate(**params)
