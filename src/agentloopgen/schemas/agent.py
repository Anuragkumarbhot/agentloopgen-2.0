```python
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class AgentBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: str = Field(default="inactive")  # active, inactive, paused, etc.


class AgentCreate(AgentBase):
    pass


class AgentResponse(AgentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
```