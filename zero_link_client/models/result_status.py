from enum import Enum


class ResultStatus(str, Enum):
    ANSWERS = "answers"
    EMPTY = "empty"
    ERROR = "error"
    FALSE = "false"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
