from enum import Enum


class ContextAssumption(str, Enum):
    GLOBAL = "global"
    LOCAL = "local"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
