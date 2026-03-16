```python
"""
FastAPI application factory for AgentLoopGen.
"""
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from agentloopgen.api.v1 import api_router
from agentloopgen.config import settings
from agentloopgen.infrastructure.database import create_db_and_tables, engine
from agentloopgen.infrastructure.redis import redis_client
from agentloopgen.utils.logger import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """
    Lifespan context manager for startup and shutdown events.
    """
    # Startup
    setup_logging()
    await create_db_and_tables()
    # Ensure Redis is connected (ping)
    await redis_client.ping()
    print("🚀 AgentLoopGen started")

    yield

    # Shutdown
    await engine.dispose()
    await redis_client.close()
    print("👋 AgentLoopGen stopped")


def create_app() -> FastAPI:
    """
    Application factory.
    """
    app = FastAPI(
        title="AgentLoopGen API",
        version=__version__,
        description="Enterprise AI Workflow Operating System",
        lifespan=lifespan,
    )

    # Include API router
    app.include_router(api_router, prefix="/api/v1")

    # Health check endpoint
    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

    # Prometheus metrics
    if settings.ENVIRONMENT != "development":
        Instrumentator().instrument(app).expose(app)

    return app


app = create_app()
```