from fastapi import FastAPI

from .elastic.tpl import get_stop, get_all_stops
from .elastic.publibike import get_station, get_all_stations
from .elastic.pollution import get_current_pollution
from .database.monster import get_all_monsters, get_monster
from .database.user import get_user
from .logic.handlers import handle_journey_register
from . import classes as c

app = FastAPI()

@app.get("/monster/{id}")
async def monsters(id: int):
    return await get_monster(monster_id=id)


@app.get("/monsters")
async def monsters():
    return await get_all_monsters()


@app.get("/users/{id}")
async def users(id: int):
    return await get_user(user_id=id)


@app.put("/users/{id}")
async def travels(id: int, journey: c.RegisterJourney):
    return await handle_journey_register(id, journey)


@app.get("/users")
def users(id: int):
    raise NotImplementedError
    # return await get_all_users()


@app.get("/pollution")
def pollution():
    return get_current_pollution()


@app.get("/stations/bike/{name}")
async def bike_stations(name: str):
    return get_station(station_name=name)


@app.get("/stations/bike")
async def bike_stations_all():
    return get_all_stations()


@app.get("/stations/tpl/{name}")
async def bus_stations(name: str):
    return get_stop(name)


@app.get("/stations/tpl")
def bus_stations_all():
    return get_all_stops()
