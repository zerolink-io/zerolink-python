from enum import Enum


class RequestType(str, Enum):
    FACT = "fact"
    QUESTION = "question"

    def __str__(self) -> str:
        return str(self.value)
