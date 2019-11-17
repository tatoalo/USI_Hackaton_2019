import asyncio
import math
import os
from typing import Tuple

import aiohttp
from backend.database.user import create_new_user_fight, get_user, update_user_fight, update_user_stats

from ..classes import Coords, JourneyType, JourneyUpdate, Monster, Pollution, RegisterJourney, User
from ..database.monster import get_all_monsters, get_monster
from ..elastic.pollution import get_current_pollution
from ..exceptions import RouteNotFoundError
from ..monster_status import choose_monster, damage, obtain_xp, update_xp_required
from .store_journey import store_journey

MAP_QUEST_URL = "http://www.mapquestapi.com/directions/v2/route"
MAP_QUEST_KEY = os.environ["MAP_QUEST_API_KEY"]


def get_monster_damage(type: JourneyType, pollution: Pollution) -> int:
    monster_damage = damage(1, pollution)
    if type == JourneyType.bus:
        monster_damage = int(monster_damage * 0.8)
    elif type == JourneyType.car:
        monster_damage = 0
    return monster_damage


def get_user_damage(fuel: float, type: JourneyType) -> int:
    user_damage = 0
    if type == JourneyType.bus:
        user_damage = int(fuel + 3)
    elif type == JourneyType.car:
        user_damage = int((fuel + 3) * 5)
    return user_damage


def get_new_level(current_xp: int, xp_required: int, current_level: int) -> Tuple[int, int, int]:
    new_level = current_level
    while current_xp >= xp_required:
        current_xp -= xp_required
        new_level += 1
        xp_required = update_xp_required(new_level)
    return new_level, current_xp, xp_required


async def update_user(user: User, monster_damage: int, user_damage: int) -> int:
    """Update user stats and fight info after a journey registration."""
    stats, fight = user.stats, user.current_fight
    new_level, new_xp, new_xp_required = stats.lvl, stats.xp, stats.xp_required
    monster_object: Monster = await get_monster(monster_id=fight.monster_id)

    # the monster was killed by performing this journey
    if fight.monster_hp - monster_damage <= 0:
        monsters = await get_all_monsters()
        monsters = [m for m in monsters if user.current_fight.monster_id != m.id]
        monster = choose_monster(monsters, user.stats.lvl)
        new_level, new_xp, new_xp_required = get_new_level(
            stats.xp + obtain_xp(monster_object), new_xp_required, new_level
        )
        await create_new_user_fight(user_id=user.id, monster=monster)
    # deduce HP from the monster, update XP for making a damage
    else:
        # add XP only in case damage was caused to the monster
        if monster_damage > 0:
            new_level, new_xp, new_xp_required = get_new_level(
                stats.xp + int(math.sqrt(obtain_xp(monster_object))), new_xp_required, new_level
            )
        await update_user_fight(user_id=user.id, new_monster_hp=fight.monster_hp - monster_damage)

    # update user depending on level (set to 100 if level changed)
    new_hp = stats.hp - user_damage if stats.lvl == new_level else 100

    # if a user died
    if new_hp <= 0:
        new_hp, new_xp = 100, 0
        new_level = new_level - 5 if new_level - 5 > 1 else 1
        new_xp_required = update_xp_required(new_level)

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

    monster_damage = get_monster_damage(journey.type, pollution)
    user_damage = get_user_damage(fuel, journey.type)

    await update_user(user, monster_damage, user_damage)

    new_usr = await get_user(user_id=user_id)
    new_monster = await get_monster(monster_id=new_usr.current_fight.monster_id)
    asyncio.create_task(
        store_journey(
            journey.type,
            Coords(lat=journey.lat_start, lon=journey.lon_start),
            Coords(lat=journey.lat_end, lon=journey.lon_end),
            distance,
            fuel,
        )
    )
    return JourneyUpdate(user=new_usr, monster=new_monster, distance=distance, fuel_saved=fuel)
