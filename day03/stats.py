from collections import Counter

from models import LogLine


def count_levels(lines: list[LogLine]) -> Counter:
    return Counter(line.level for line in lines)


def top_errors(lines: list[LogLine], n: int = 5) -> list[tuple[str, int]]:
    errors = Counter(line.message for line in lines if line.is_error)
    return errors.most_common(n)


def count_by_hour(lines: list[LogLine]) -> Counter:
    return Counter(line.hour for line in lines)
