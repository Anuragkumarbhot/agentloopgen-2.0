```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from agentloopgen.infrastructure.database import get_db
from agentloopgen.schemas.agent import AgentCreate, AgentResponse
from agentloopgen.services import agent_service

router = APIRouter()


@router.post("/", response_model=AgentResponse)
async def create_agent(
    agent: AgentCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a new agent."""
    return await agent_service.create_agent(db, agent)


@router.get("/{agent_id}", response_model=AgentResponse)
async def get_agent(
    agent_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get agent by ID."""
    agent = await agent_service.get_agent(db, agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent


# Additional endpoints (list, update, delete, etc.) would go here
```