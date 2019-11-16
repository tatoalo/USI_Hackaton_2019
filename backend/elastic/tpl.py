from typing import Generator
from .core import search_index
from ..classes import Bus, Coords

INDEX_NAME = "tpl_stops"


def get_all_stops() -> Generator[Bus, None, None]:
    for _, record in search_index(index_name=INDEX_NAME, search_definition={"size": 1000}):
        yield Bus(name=record["name"], address=record["name"], id=record["number"], coords=Coords(**record["location"]))


def get_stop(station_name: str) -> Bus:
    _, record = next(
        search_index(index_name=INDEX_NAME, search_definition={"query": {"match": {"name": station_name}}})
    )
    return Bus(name=record["name"], address=record["name"], id=record["number"], coords=Coords(**record["location"]))
