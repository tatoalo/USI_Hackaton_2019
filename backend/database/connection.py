from functools import wraps
from asyncpgsa import pg


def database_connection(func):
    @wraps(func)
    async def inner(connection=None, **kwargs):
        if connection is not None:
            return await func(connection=connection, **kwargs)
        async with pg.begin() as conn:
            return await func(connection=conn, **kwargs)

    return inner
