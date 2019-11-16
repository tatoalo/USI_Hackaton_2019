from typing import List
from asyncpg import Record
from sqlalchemy import select, literal_column

from ..exceptions import ObjectNotFound


def build_query(selectable, condition=None):
    query = select(selectable)
    if condition is not None:
        query = query.where(condition)
    return query


async def get_one(connection, selectable, condition=None):
    return await fetch_one(connection, query=build_query(selectable, condition))


async def fetch_more(connection, selectable, condition=None):
    return await connection.fetch(build_query(selectable, condition=condition))


async def fetch_one(connection, *, query):
    """Retrieves one record from the DB. If record does not exist, raises an Exception."""
    result = await connection.fetchrow(query)
    if result is None:
        raise ObjectNotFound
    return result


async def create(connection, table, **values) -> Record:
    return await connection.fetchrow(table.insert().values(**values).returning(literal_column("*")))


async def update(connection, table, condition, **values) -> List[Record]:
    query = table.update().where(condition).values(**values).returning(literal_column("*"))
    return await connection.fetch(query)
