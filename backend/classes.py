from pydantic import BaseModel

"""
Auxiliar classes.
"""

class Coords(BaseModel):
    """
    Class that returns the coordinates.
    """
    lat: float
    lon: float

class Stats(BaseModel):
    """
    Class that returns the stats of the user.
    """
    xp: int
    xp_required: int
    lvl: int
    hp: int

class Current_fight(BaseModel):
    """
    Class that returns the current fight against a boss for a user.
    """
    monster_id: int
    monster_hp: int

"""
Principal classes.
"""

class Bus(BaseModel):
    """
    Class that returns the information of a bus station.
    """
    id: int
    name: str
    address: str
    coords: Coords

class Monster(BaseModel):
    """
    Class that returns the information of a monster without state.
    """
    id: int
    max_hp: int
    icon:str
    name:str
    lvl:int

class Bikes(BaseModel):
    """
    Class that returns the information of bike station.
    """
    id: int
    name: str
    address: str
    coords: Coords

class Users(BaseModel):
  """
  Class that returns the information of a user.
  """
  name: str
  icon: str
  stats: Stats
  current_fight: Current_fight

class Pollution(BaseModel):
   """Class that returns the actual pollution."""
   NO2: float
   NO: float
   O3: float
   PM10: float
