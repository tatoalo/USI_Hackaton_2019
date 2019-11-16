from enum import Enum

from pydantic import BaseModel


"""
Auxiliar classes.
"""


class Coords(BaseModel):
    """Class that returns the coordinates."""

    lat: str
    lon: str


class Stats(BaseModel):
    """Class that returns the stats of the user."""

    xp: int
    xp_required: int
    lvl: int
    hp: int


class CurrentFight(BaseModel):
    """Class that returns the current fight against a boss for a user."""

    monster_id: int
    monster_hp: int


class JourneyType(Enum):
    bike = "bike"
    walk = "walk"
    bus = "bus"
    car = "car"


"""
Principal classes.
"""


class Bus(BaseModel):
    """Class that returns the information of a bus station."""

    id: int
    name: str
    address: str
    coords: Coords


class Monster(BaseModel):
    """Class that returns the information of a monster without state."""

    id: int
    max_hp: int
    icon: str
    name: str
    lvl: int


class Bikes(BaseModel):
    """Class that returns the information of bike station."""

    id: int
    name: str
    address: str
    coords: Coords


class User(BaseModel):
    """Class that returns the information of a user."""

    id: int
    name: str
    icon: str
    stats: Stats
    current_fight: CurrentFight


class Pollution(BaseModel):
    """Class that returns the actual pollution."""

    NO2: float
    NO: float
    O3: float
    PM10: float


class RegisterJourney(BaseModel):
    type: str
    lat_start: float
    lon_start: float
    lat_end: float
    lon_end: float


class JourneyUpdate(BaseModel):
    user: User
    distance: float
    fuel_saved: float
