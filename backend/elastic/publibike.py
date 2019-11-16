from typing import Generator
from .core import search_index
from ..classes import Bikes, Coords

INDEX_NAME = "publibike_stations"


def get_all_stations() -> Generator[Bikes, None, None]:
    for _, record in search_index(index_name=INDEX_NAME, search_definition={"size": 100}):
        yield Bikes(**record, coords=Coords(**record["location"]))


def get_station(station_name: str) -> Bikes:
    _, record = next(
        search_index(index_name=INDEX_NAME, search_definition={"query": {"match": {"name": station_name}}})
    )
    return Bikes(**record, coords=Coords(**record["location"]))
