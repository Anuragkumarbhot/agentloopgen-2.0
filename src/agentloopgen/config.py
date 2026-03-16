```python
from typing import Optional

from pydantic import Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Database
    DATABASE_URL: PostgresDsn = Field(
        default="postgresql+asyncpg://agentloopgen:agentloopgen@localhost/agentloopgen",
        description="PostgreSQL asyncpg connection string",
    )

    # Redis
    REDIS_URL: RedisDsn = Field(
        default="redis://localhost:6379/0",
        description="Redis connection string",
    )

    # Environment
    ENVIRONMENT: str = Field(default="development", description="Runtime environment")

    # Security
    SECRET_KEY: str = Field(default="change-me-in-production", description="JWT secret")
    ALGORITHM: str = Field(default="HS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, description="JWT expiry")

    # Kubernetes (optional, for scaling)
    KUBERNETES_SERVICE_HOST: Optional[str] = Field(default=None)
    KUBERNETES_SERVICE_PORT: Optional[str] = Field(default=None)

    # Prometheus
    PROMETHEUS_MULTIPROC_DIR: str = Field(default="/tmp", description="Directory for prometheus multiproc metrics")


settings = Settings()
```