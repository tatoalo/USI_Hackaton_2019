from fastapi import APIRouter

from . import classes as c
from .database.monster import get_all_monsters, get_monster
from .database.user import get_user
from .elastic.pollution import get_current_pollution
from .elastic.publibike import get_all_stations, get_station
from .elastic.tpl import get_all_stops, get_stop
from .logic.process_journey import handle_journey_register

app_router = APIRouter()


@app_router.get("/monsters/{id}")
async def monsters(id: int):
    return await get_monster(monster_id=id)


@app_router.get("/monsters")
async def monsters():
    return await get_all_monsters()


@app_router.get("/users/{id}")
async def users(id: int):
    return await get_user(user_id=id)


@app_router.put("/users/{id}")
async def travels(id: int, journey: c.RegisterJourney):
    return await handle_journey_register(id, journey)


@app_router.get("/users")
def users():
    raise NotImplementedError


@app_router.get("/pollution")
def pollution():
    return get_current_pollution()


@app_router.get("/stations/bike/{name}")
async def bike_stations(name: str):
    return get_station(station_name=name)


@app_router.get("/stations/bike")
async def bike_stations_all():
    return get_all_stations()


@app_router.get("/stations/tpl/{name}")
async def bus_stations(name: str):
    return get_stop(name)


@app_router.get("/stations/tpl")
def bus_stations_all():
    return get_all_stops()
