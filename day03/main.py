from log_parser import parse_file
from stats import count_levels, top_errors, count_by_hour


def main():
    lines = parse_file("day02/app.log")
    print(f"첫 줄: {lines[0]}")

    print("레벨별 건수")
    for level, count in count_levels(lines).items():
        print(f" {level}: {count}")

    print("자주 나온 에러")
    for message, count in top_errors(lines, n=3):
        print(f" {count}회 {message}")

    print("시간대별 건수")
    for hour, count in sorted(count_by_hour(lines).items()):
        print(f" {hour:02d}시: {count}")


if __name__ == "__main__":
    main()
