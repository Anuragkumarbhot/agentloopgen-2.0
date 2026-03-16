```python
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from agentloopgen.infrastructure.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    description = Column(String, nullable=True)
    status = Column(String, default="inactive")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships (example)
    # workflows = relationship("Workflow", back_populates="agent")
```