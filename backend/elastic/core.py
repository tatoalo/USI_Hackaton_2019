from typing import Dict, Any, List

from elasticsearch import Elasticsearch
from ..settings import BACKEND_SETTINGS

es_connection = Elasticsearch(
    [BACKEND_SETTINGS["elastic_host"]],
    http_auth=[BACKEND_SETTINGS["elastic_username"], BACKEND_SETTINGS["elastic_password"]],
)


def search_index(index_name: str, search_definition: Dict[str, Any] = None) -> List[Dict]:
    response = es_connection.search(index=[index_name], body=search_definition)
    for record in response["hits"]["hits"]:
        yield record["_id"], record["_source"]
