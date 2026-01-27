from typing import Union, Literal
from pydantic import BaseModel
from .rich_repr import RichReprMixin

class AIChunkText(RichReprMixin, BaseModel):
    type: Literal["text"] = "text"
    text: str

class AIChunkFile(RichReprMixin, BaseModel):
    type: Literal["file"] = "file"
    name: str
    mimetype: str
    bytes: bytes

class AIChunkImageURL(RichReprMixin, BaseModel):
    type: Literal["image"] = "image"
    url: str

class AIChunkToolCall(RichReprMixin, BaseModel):
    type: Literal["tool_call"] = "tool_call"
    id: str
    name: str
    arguments: dict[str, object]


AIChunk = Union[AIChunkText, AIChunkFile, AIChunkImageURL, AIChunkToolCall]