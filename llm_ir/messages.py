from pydantic import BaseModel, Field

from .chunks import AIChunk
from .roles import AIRoles


class AIMessage(BaseModel):

    role: AIRoles
    chunks: list[AIChunk] = Field(default_factory=list[AIChunk])

class AIMessageToolResponse(AIMessage):

    id: str
    name: str
    role: AIRoles = AIRoles.TOOL


