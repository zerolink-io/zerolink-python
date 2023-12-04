from enum import Enum


class TemporalAssumption(str, Enum):
    ABSTRACT = "abstract"
    CURRENT = "current"
    HISTORICAL = "historical"

    def __str__(self) -> str:
        return str(self.value)
