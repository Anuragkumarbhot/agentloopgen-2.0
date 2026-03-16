```python
from fastapi import APIRouter

from agentloopgen.api.v1 import agents, workflows, telemetry, governance, admin

api_router = APIRouter()

api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
api_router.include_router(workflows.router, prefix="/workflows", tags=["workflows"])
api_router.include_router(telemetry.router, prefix="/telemetry", tags=["telemetry"])
api_router.include_router(governance.router, prefix="/governance", tags=["governance"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
```