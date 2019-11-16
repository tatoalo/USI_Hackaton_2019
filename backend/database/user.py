from sqlalchemy import select, join, literal_column

from . import core
from .models import User, UserStatistics, Fight
from .connection import database_connection
from ..classes import Monster, User as IntegrationUser, Stats, CurrentFight

USER_STATISTICS_JOIN = join(User, UserStatistics, User.c.id == UserStatistics.c.user_id)
USER_STATISTICS_FIGHT_JOIN = join(USER_STATISTICS_JOIN, Fight, User.c.id == Fight.c.user_id)


@database_connection
async def get_user(connection, *, user_id: int) -> IntegrationUser:
    query = (
        select((*User.c, *UserStatistics.c, Fight.c.monster_id, Fight.c.monster_hp))
        .select_from(USER_STATISTICS_FIGHT_JOIN)
        .where(User.c.id == user_id)
    )
    user = await core.fetch_one(connection, query=query)
    return IntegrationUser(**user, stats=Stats(**user, lvl=user["level"]), current_fight=CurrentFight(**user))


@database_connection
async def create_user(connection, *, user_name: str, user_icon: str, monster: Monster) -> IntegrationUser:
    async with connection.transaction():
        user = await connection.fetchrow(
            User.insert().values(name=user_name, icon=user_icon).returning(literal_column("*"))
        )
        user_statistics = await connection.fetchrow(
            UserStatistics.insert().values(user_id=user["id"], xp_required=10).returning(literal_column("*"))
        )
        user_fight = await connection.fetchrow(
            Fight.insert()
            .values(user_id=user["id"], monster_id=monster.id, monster_hp=monster.max_hp)
            .returning(literal_column("*"))
        )
    return IntegrationUser(**user, stats=Stats(**user_statistics), current_fight=CurrentFight(**user_fight))


@database_connection
async def update_user_stats(connection, *, user_id: int, **attributes) -> Stats:
    """Update statistics of the user."""
    response = await core.update(connection, UserStatistics, UserStatistics.c.user_id == user_id, **attributes)
    return Stats(**response[0])


@database_connection
async def update_user_fight(connection, *, user_id: int, new_monster_hp: int) -> CurrentFight:
    """Update the HP of the current monster."""
    response = await core.update(connection, Fight, Fight.c.user_id == user_id, monster_hp=new_monster_hp)
    return CurrentFight(**response[0])


@database_connection
async def create_new_user_file(connection, *, user_id: int, monster: Monster) -> CurrentFight:
    """Create a new fight for a user by updating their Fight record and setting monster's HP to its max value."""
    response = await core.update(
        connection, Fight, Fight.c.user_id == user_id, monster_id=monster.id, monster_hp=monster.max_hp
    )
    return CurrentFight(**response[0])
