from sqlalchemy import select, literal_column

from .exceptions import ObjectNotFound


def build_query(selectable, condition=None):
    query = select(selectable)
    if condition is not None:
        query = query.where(condition)
    return query


async def fetch_one(connection, *, query):
    """Retrieves one record from the DB. If record does not exist, raises an Exception."""
    result = await connection.fetchrow(query)
    if result is None:
        raise ObjectNotFound
    return result


async def update(connection, table, condition, **values):
    query = table.update().where(condition).values(**values).returning(literal_column("*"))
    return await connection.fetch(query)
