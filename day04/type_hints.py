def average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


def find_user(user_id: int) -> str | None:
    users = {1: "kim", 2: "lee"}
    return users.get(user_id)


print(average([80, 90, 100]))
print(find_user(1), find_user(99))
