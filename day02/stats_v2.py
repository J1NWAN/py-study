# 버전 2: Python 스타일 (컴프리헨션과 Counter)
from collections import Counter
from pathlib import Path

lines = Path("day02/app.log").read_text(encoding="utf-8").splitlines()
rows = [line.split(" ", 3) for line in lines]  # 날짜, 시간, 레벨, 메시지

level_counts = Counter(row[2] for row in rows)
error_counts = Counter(row[3] for row in rows if row[2] == "ERROR")
warn_counts = Counter(row[3] for row in rows if row[2] == "WARN")

print("레벨별 건수")
for level, count in level_counts.items():
    print(f" {level}: {count}")

print("자주 나온 에러")
for message, count in error_counts.most_common(5):
    print(f" {count}회 {message}")

print("자주 나온 경고")
for message, count in warn_counts.most_common(5):
    print(f" {count}회 {message}")
