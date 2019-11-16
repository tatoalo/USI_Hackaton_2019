from asyncpgsa import pg
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response

from aiohttp import ClientConnectionError, ClientResponseError
from migrations.mocked_data.insert_mock_data import insert_data

from . import main
from .exceptions import DatabaseException, ObjectNotFound, RouteNotFoundError
from .settings import BACKEND_SETTINGS


def create_app():
    app = FastAPI()
    app.include_router(main.app_router)

    @app.on_event("startup")
    async def startup():
        await pg.init(dsn=BACKEND_SETTINGS["database_url"], min_size=1, max_size=5)
        await insert_data()

    return app


app_instance = create_app()


@app_instance.middleware("http")
async def exception_middleware(request: Request, call_next) -> Response:
    try:
        response = await call_next(request)
    except ObjectNotFound:
        return PlainTextResponse("Requested object does not exist.", status_code=404)
    except RouteNotFoundError:
        return PlainTextResponse("Route does not exist.", status_code=404)
    except DatabaseException:
        return PlainTextResponse("Unexpected database error.", status_code=500)
    except ClientResponseError as exc:
        return PlainTextResponse(f"Mapping service error {exc.status}", status_code=exc.message)
    except ClientConnectionError:
        return PlainTextResponse("Mapping service not available.", status_code=503)

    return response
