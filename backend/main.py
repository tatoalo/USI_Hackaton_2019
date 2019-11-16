from .elastic.tpl import get_stop, get_all_stops
from .elastic.publibike import get_station, get_all_stations
from .elastic.pollution import get_current_pollution
from .database.monster import get_all_monsters, get_monster
from .database.user import get_user
from .logic.handlers import handle_journey_register
from . import classes as c
from fastapi import APIRouter

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
def users(id: int):
    raise NotImplementedError
    # return await get_all_users()


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
