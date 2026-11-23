from pathlib import Path

from models import LogLine


def parse_line(line: str) -> LogLine:
    date, time, level, message = line.strip().split(" ", 3)
    return LogLine(date, time, level, message)


def parse_file(path: str) -> list[LogLine]:
    text = Path(path).read_text(encoding="utf-8")
    return [parse_line(line) for line in text.splitlines() if line.strip()]
