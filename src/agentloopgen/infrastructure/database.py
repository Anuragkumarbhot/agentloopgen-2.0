```python
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from agentloopgen.config import settings

# Create async engine
engine = create_async_engine(
    str(settings.DATABASE_URL),
    echo=settings.ENVIRONMENT == "development",
    future=True,
)

# Session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base class for models
Base = declarative_base()


async def create_db_and_tables():
    """
    Create tables if they don't exist (for development).
    In production, use Alembic migrations.
    """
    if settings.ENVIRONMENT == "development":
        async with engine.begin() as conn:
            # Uncomment to auto-create tables (not recommended for production)
            # await conn.run_sync(Base.metadata.create_all)
            pass


async def get_db() -> AsyncSession:
    """
    Dependency to get DB session.
    """
    async with AsyncSessionLocal() as session:
        yield session
```