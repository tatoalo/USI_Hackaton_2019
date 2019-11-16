from typing import List

from .models import Monster
from ..classes import Monster as IntegrationMonster
from .connection import database_connection
from . import core


@database_connection
async def get_all_monsters(connection) -> List[Monster]:
    response = await core.fetch_more(connection, [Monster])
    return [IntegrationMonster(**row) for row in response]


@database_connection
async def get_monster(connection, *, monster_id: int) -> Monster:
    response = await core.get_one(connection, [Monster], condition=Monster.c.id == monster_id)
    return IntegrationMonster(**response)


@database_connection
async def create_monster(connection, *, monster: IntegrationMonster) -> IntegrationMonster:
    response = await core.create(
        connection, Monster, name=monster.name, level=monster.lvl, icon=monster.icon, maximum_hp=monster.max_hp
    )
    return IntegrationMonster(**response)
