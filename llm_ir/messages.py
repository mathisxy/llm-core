from typing import List
from pydantic import BaseModel, Field

from .chunks import AIChunk
from .roles import AIRoles


class AIMessage(BaseModel):

    role: AIRoles
    chunks: List[AIChunk] = Field(default_factory=List[AIChunk])


