from typing import Union, Literal
from pydantic import BaseModel

class AIChunkText(BaseModel):
    type: Literal["text"] = "text"
    text: str

class AIChunkFile(BaseModel):
    type: Literal["file"] = "file"
    name: str
    mimetype: str
    bytes: bytes

class AIChunkImageURL(BaseModel):
    type: Literal["image"] = "image"
    url: str

class AIChunkToolCall(BaseModel):
    id: str
    name: str
    arguments: dict[str, object]
    

AIChunk = Union[AIChunkText, AIChunkFile, AIChunkImageURL]