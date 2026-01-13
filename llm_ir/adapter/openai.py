from ..messages import AIMessage
from ..chunks import AIChunk, AIChunkText, AIChunkImageURL, AIChunkFile
import base64

def to_openai(messages: list[AIMessage]) -> list[dict[str, str|dict[str, str]|list[dict[str, str]]]]:
    

    result: list[dict[str, str|dict[str, str]|list[dict[str, str]]]] = []
    for message in messages:
        role = message.role.value
        result.append({
            "role": role,
            "content": [
                chunk_to_openai(chunk) for chunk in message.chunks
            ]
        })
    return result


def chunk_to_openai(chunk: AIChunk) -> dict[str, str]:

    match chunk:
        case AIChunkText():
            return {
                "type": "text",
                "text": chunk.text,
            }
        case AIChunkImageURL():
            return {
                "type": "image_url",
                "image_url": chunk.url,
            }
        case AIChunkFile():
            if chunk.mimetype.startswith("image/"):
                base64_data = base64.b64encode(chunk.bytes).decode('utf-8')
                return {
                    "type": "image_url",
                    "image_url": f"data:{chunk.mimetype};base64,{base64_data}",
                }
            else:
                raise ValueError(f"Unsupported file type for OpenAI: {chunk.mimetype}")
        case _:
            raise ValueError(f"Unsupported chunk type: {type(chunk)}")