from enum import Enum


class ResponseType(str, Enum):
    ANSWER = "answer"
    ERROR = "error"
    FACTS = "facts"

    def __str__(self) -> str:
        return str(self.value)
