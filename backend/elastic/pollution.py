from .core import search_index
from ..classes import Pollution
from datetime import datetime, timedelta


def get_current_pollution() -> Pollution:
    current_time = datetime.now()
    _, record = next(
        search_index(
            index_name="pollution",
            search_definition={
                "size": 1,
                "query": {
                    "range": {
                        "@timestamp": {
                            "gte": current_time.isoformat(),
                            "lte": (current_time + timedelta(minutes=30)).isoformat(),
                        }
                    }
                },
            },
        )
    )
    return Pollution(
        NO=record["nitrogen_monoxide"],
        NO2=record["nitrogen_dioxide"],
        O3=record["ozone"],
        PM10=record["fine_particles"],
    )
