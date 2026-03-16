```python
import redis.asyncio as redis
from redis.asyncio import Redis

from agentloopgen.config import settings

# Redis client
redis_client: Redis = redis.from_url(str(settings.REDIS_URL), decode_responses=True)


async def get_redis() -> Redis:
    """
    Dependency to get Redis client.
    """
    return redis_client
```