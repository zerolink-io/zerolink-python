from enum import Enum


class ExtractModel(str, Enum):
    BASE = "base"
    FINANCE = "finance"
    GENOMICS = "genomics"
    INSURANCE = "insurance"
    LEGAL = "legal"

    def __str__(self) -> str:
        return str(self.value)
