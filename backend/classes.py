from pydantic import BaseModel

class Bus(BaseModel):
    id: int
    name: str
    address: str
    lat: float
    lon: float

class Monster(BaseModel):
    pass

class Bikes(BaseModel):
    pass

class Users(BaseModel):
    pass

class Pollution(BaseModel):
    pass
