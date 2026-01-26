from pydantic import BaseModel
from typing import Any

class Tool(BaseModel):
    name: str
    description: str
    input_schema: dict[str, Any]

