from enum import Enum


class SpatialAssumption(str, Enum):
    EARTH = "earth"
    UNIVERSE = "universe"

    def __str__(self) -> str:
        return str(self.value)
