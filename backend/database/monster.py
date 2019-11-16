from typing import List

from .models import Monster
from ..classes import Monster as IntegrationMonster
from .connection import database_connection
from . import core


@database_connection
async def get_all_monsters(connection) -> List[IntegrationMonster]:
    response = await core.fetch_more(connection, [Monster])
    return [IntegrationMonster(**row, lvl=row["level"], max_hp=row["maximum_hp"]) for row in response]


@database_connection
async def get_monster(connection, *, monster_id: int) -> IntegrationMonster:
    response = await core.get_one(connection, [Monster], condition=Monster.c.id == monster_id)
    return IntegrationMonster(**response, lvl=response["level"], max_hp=response["maximum_hp"])


@database_connection
async def create_monster(connection, *, monster: IntegrationMonster) -> IntegrationMonster:
    response = await core.create(
        connection, Monster, name=monster.name, level=monster.lvl, icon=monster.icon, maximum_hp=monster.max_hp
    )
    return IntegrationMonster(**response, lvl=response["level"], max_hp=response["maximum_hp"])
