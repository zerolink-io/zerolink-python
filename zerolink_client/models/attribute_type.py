from enum import Enum


class AttributeType(str, Enum):
    DATE = "DATE"
    DATETIME = "DATETIME"
    DIMENSIONAL_QUANTITY = "DIMENSIONAL_QUANTITY"
    DIMENSIONLESS_QUANTITY = "DIMENSIONLESS_QUANTITY"
    GPS_COORDINATES = "GPS_COORDINATES"
    MONOLINGUAL_TEXT = "MONOLINGUAL_TEXT"
    URL = "URL"

    def __str__(self) -> str:
        return str(self.value)
