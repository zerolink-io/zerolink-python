from enum import Enum


class WorldAssumption(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    PARTIAL = "partial"

    def __str__(self) -> str:
        return str(self.value)
