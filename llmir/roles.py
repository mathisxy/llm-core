from enum import StrEnum


class AIRoles(StrEnum):

    USER = "user"
    MODEL = "assistant"
    SYSTEM = "system"
    TOOL = "tool"