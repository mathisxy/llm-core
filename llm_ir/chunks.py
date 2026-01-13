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

AIChunk = Union[AIChunkText, AIChunkFile, AIChunkImageURL]