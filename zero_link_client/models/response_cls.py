from enum import Enum


class ResponseCls(str, Enum):
    AFFIRMATIVE = "affirmative"
    NEGATIVE = "negative"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
