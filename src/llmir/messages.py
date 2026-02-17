from pydantic import BaseModel, Field
from typing import Literal
from .chunks import AIChunks
from .roles import AIRoles

class AIMessage(BaseModel):

    role: Literal[AIRoles.USER, AIRoles.MODEL, AIRoles.SYSTEM]
    chunks: list[AIChunks] = Field(default_factory=list[AIChunks])

class AIMessageToolResponse(BaseModel):

    role: Literal[AIRoles.TOOL] = AIRoles.TOOL
    chunks: list[AIChunks] = Field(default_factory=list[AIChunks])
    id: str
    name: str

AIMessages = AIMessage | AIMessageToolResponse