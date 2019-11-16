from fastapi import FastAPI
from . import classes as c

app = FastAPI()

@app.get("/monster/{id}")
def monsters(id:int):
    """
    Get monster details
    """
    pass

@app.get("/monster")
def monsters():
    """
    Get all monsters
    """
    pass

@app.get("/users/{id}")
def users(id:int):
    """
    Get user details
    """
    pass

@app.put("/users/")
def travels(id:int):
    """
    Register travel of the user
    """
    pass

@app.get("/users")
def users(id:int):
    """
    Get all users
    """
    pass

@app.get("/pollution")
def pollution():
    """
    Get pollution values
    """
    pass

@app.get("/stations/bike/{id}")
def bike_stations(id:int):
    """
    Get bike station detail
    """
    pass

@app.get("/stations/bike")
def bike_stations_all():
    """
    Get all bike station detail
    """
    pass

@app.get("/stations/tpl/{id}")
def bus_stations(id:int):
    """
    Get bus station detail
    """
    pass

@app.get("/stations/tpl")
def bus_stations_all():
    """
    Get all bus station detail
    """
    pass
