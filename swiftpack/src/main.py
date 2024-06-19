"""Top-level module for the FastAPI application."""

from functools import lru_cache

from fastapi import Depends, FastAPI
from starlette_prometheus import metrics, PrometheusMiddleware

from swiftpack.src.config import Settings
from swiftpack.src.db import get_session, init_db
from swiftpack.src.routers.api import router as api_router


@lru_cache
def get_settings():
    return Settings()


# Factory method for creating the FastAPI app
def create_app() -> FastAPI:
    app = FastAPI()
    # settings: Settings = get_settings()
    app.state.settings = get_settings()

    # Dependency injection for the session
    @app.on_event("startup")
    async def on_startup():
        await init_db()

    # Dependency injection for the session
    @app.on_event("shutdown")
    async def on_shutdown():
        await get_session().close()

    @app.get("/info")
    async def info():
        return {
            "app_name": app.state.settings.app_name,
            "log_level": app.state.settings.log_level,
            "api_prefix": app.state.settings.api_prefix,
            "database_type": app.state.settings.database_type,
        }

    # health endpoint
    @app.get("/health")
    async def health():
        """Super awesome health check endpoint :)"""
        return {"status": "ok"}

    # add prometheus middleware
    app.add_middleware(PrometheusMiddleware)
    app.add_route("/metrics", metrics)

    @app.get(f"{app.state.settings.api_prefix}/ping")
    async def pong():
        return {"ping": "pong!"}

    # Include the API router
    app.include_router(
        api_router,
        prefix=f"{app.state.settings.api_prefix}/songs",
        tags=["songs"],
        dependencies=[Depends(get_session)],
        responses={
            200: {"description": "Success"},
            201: {"description": "Created"},
            404: {"description": "Not found"},
            500: {"description": "Internal Server Error"},
        },
    )

    return app
