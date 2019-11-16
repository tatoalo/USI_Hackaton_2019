from functools import wraps
import asyncpgsa

from ..settings import BACKEND_SETTINGS


async def create_database_pool():
    return await asyncpgsa.create_pool(dsn=BACKEND_SETTINGS["database_url"], min_size=1, max_size=5)


def database_connection(func):
    @wraps(func)
    async def inner(connection=None, **kwargs):
        if connection is not None:
            return await func(connection=connection, **kwargs)
        pool = await create_database_pool()
        async with pool.acquire() as conn:
            return await func(connection=conn, **kwargs)

    return inner
