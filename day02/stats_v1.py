# 버전 1: Java 스타일 그대로(for문과 dict)
level_counts = {}
error_counts = {}

with open("day02/app.log", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(" ", 3)  # 날짜, 시간, 레벨, 메시지
        level = parts[2]
        message = parts[3]

        if level not in level_counts:
            level_counts[level] = 0
        level_counts[level] += 1

        if level == "ERROR":
            if message not in error_counts:
                error_counts[message] = 0
            error_counts[message] += 1

print("레벨별 건수")
for level, count in level_counts.items():
    print(f"{level} : {count}")

print("자주 나온 에러")
ranked = sorted(error_counts.items(), key=lambda pair: pair[1], reverse=True)
for message, count in ranked[:5]:
    print(f"{message}회 {count}")
