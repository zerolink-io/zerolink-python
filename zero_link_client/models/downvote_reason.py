from enum import Enum


class DownvoteReason(str, Enum):
    INACCURATE = "inaccurate"
    INAPPROPRIATE = "inappropriate"
    INCOMPLETE = "incomplete"
    OFF_TOPIC = "off-topic"

    def __str__(self) -> str:
        return str(self.value)
