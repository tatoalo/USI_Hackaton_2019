from typing import Dict, List
from asyncpg import Record
from sqlalchemy import select, join, literal_column

from . import core
from .models import User, UserStatistics, Fight
from .connection import database_connection
from ..classes import Monster
from ..utils import compute_monster_hp

USER_STATISTICS_JOIN = join(User, UserStatistics, User.c.id == UserStatistics.c.user_id)
USER_STATISTICS_FIGHT_JOIN = join(USER_STATISTICS_JOIN, Fight, User.c.id == Fight.c.user_id)


@database_connection
async def get_user(connection, *, user_id: int, include_fight: bool = False) -> Record:
    on_join = USER_STATISTICS_FIGHT_JOIN if include_fight else USER_STATISTICS_JOIN
    on_select = (*User.c, *UserStatistics.c, *Fight.c) if include_fight else (*User.c, *UserStatistics.c)
    query = select(on_select).select_from(on_join).where(User.c.id == user_id)
    return await core.fetch_one(connection, query=query)


@database_connection
async def create_user(connection, *, user_name: str, user_icon: str, monster: Monster) -> Dict:
    async with connection.transaction():
        user = await connection.fetchrow(
            User.insert().values(name=user_name, icon=user_icon).returning(literal_column("*"))
        )
        user_statistics = await connection.fetchrow(
            UserStatistics.insert().values(user_id=user["id"], xp_required=10).returning(literal_column("*"))
        )
        user_fight = await connection.fetchrow(
            Fight.insert()
            .values(user_id=user["id"], monster_id=monster.id, monster_hp=compute_monster_hp(monster.lvl))
            .returning(literal_column("*"))
        )
    return {**user, **user_statistics, **user_fight}


@database_connection
async def update_user_stats(connection, *, user_id: int, **attributes) -> List[Record]:
    return await core.update(connection, UserStatistics, UserStatistics.c.user_id == user_id, **attributes)


@database_connection
async def update_user_fight(connection, *, user_id: int, monster: Monster) -> List[Record]:
    return await core.update(
        connection, Fight, Fight.c.user_id == user_id, monster_id=monster.id, monster_hp=compute_monster_hp(monster.lvl)
    )
