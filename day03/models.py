from dataclasses import dataclass


@dataclass
class LogLine:
    data: str
    time: str
    level: str
    message: str

    @property
    def is_error(self) -> bool:
        return self.level == "ERROR"

    @property
    def hour(self) -> int:
        return int(self.time[:2])
