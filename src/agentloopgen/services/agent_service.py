```python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from agentloopgen.models.agent import Agent
from agentloopgen.schemas.agent import AgentCreate


async def create_agent(db: AsyncSession, agent_in: AgentCreate) -> Agent:
    """Create a new agent."""
    agent = Agent(**agent_in.model_dump())
    db.add(agent)
    await db.commit()
    await db.refresh(agent)
    return agent


async def get_agent(db: AsyncSession, agent_id: int) -> Agent | None:
    """Get agent by ID."""
    result = await db.execute(select(Agent).where(Agent.id == agent_id))
    return result.scalar_one_or_none()
```