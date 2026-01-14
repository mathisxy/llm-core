from typing import TypedDict, Literal, Union

from ..messages import AIMessage
from ..chunks import AIChunk, AIChunkText, AIChunkImageURL, AIChunkFile
import base64


class TextContent(TypedDict):
    type: Literal["text"]
    text: str


class ImageUrlContent(TypedDict):
    type: Literal["image_url"]
    image_url: dict[str, str]



ContentItem = Union[TextContent, ImageUrlContent]


def to_openai(messages: list[AIMessage]) -> list[dict[str, str | list[ContentItem]]]:
    

    result: list[dict[str, str | list[ContentItem]]] = []
    for message in messages:
        role = message.role.value
        result.append({
            "role": role,
            "content": [
                chunk_to_openai(chunk) for chunk in message.chunks
            ]
        })
    return result


def chunk_to_openai(chunk: AIChunk) -> ContentItem:

    match chunk:
        case AIChunkText():
            return TextContent(
                type="text",
                text=chunk.text,
            )
        case AIChunkImageURL():
            return ImageUrlContent(
                type="image_url",
                image_url={
                    "url": chunk.url,
                }
            )
        case AIChunkFile():
            if chunk.mimetype.startswith("image/"):
                base64_data = base64.b64encode(chunk.bytes).decode('utf-8')
                return ImageUrlContent(
                    type= "image_url",
                    image_url= {
                        "url": f"data:{chunk.mimetype};base64,{base64_data}",
                    }
                )
            else:
                raise ValueError(f"Unsupported file type for OpenAI: {chunk.mimetype}")
        case _:
            raise ValueError(f"Unsupported chunk type: {type(chunk)}")