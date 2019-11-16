from typing import List
from asyncpg import Record

from .models import Monster
from ..classes import Monster as MonsterIntegrationClass
from .connection import database_connection
from . import core


@database_connection
async def get_all_monsters(connection) -> List[Record]:
    return await core.fetch_more(connection, [Monster])


@database_connection
async def create_monster(connection, *, monster: MonsterIntegrationClass) -> Record:
    return await core.create(connection, Monster, name=monster.name, level=monster.lvl, icon=monster.icon)
