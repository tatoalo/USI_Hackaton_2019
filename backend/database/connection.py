from functools import wraps
import asyncpgsa

from ..settings import BASE_SETTINGS

POOL = asyncpgsa.create_pool(dns=BASE_SETTINGS["database_url"], min_size=1, max_size=5)


def database_connection(func):
    @wraps(func)
    async def inner(connection=None, **kwargs):
        if connection is not None:
            return await func(connection=connection, **kwargs)
        async with POOL.acquire() as conn:
            return await func(connection=conn, **kwargs)

    return inner
