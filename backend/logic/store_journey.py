import json
from datetime import datetime

from ..classes import Coords, JourneyType
from ..elastic.core import insert_data


async def store_journey(type: JourneyType, start_coords: Coords, end_coords: Coords, distance: float, fuel: float):
    current_time = datetime.now()
    dict_data = {
        "type": type.value,
        "start_location": {"lat": start_coords.lat, "lon": start_coords.lon},
        "end_location": {"lat": end_coords.lat, "lon": end_coords.lon},
        "distance": distance,
        "fuel": fuel,
        "@timestamp": current_time.timestamp(),
    }
    insert_data("journeys", current_time.timestamp(), json.dumps(dict_data))
