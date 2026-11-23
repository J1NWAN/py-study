def greet(name, greeting="안녕하세요", *, shout=False):
    """greeting은 기본값이 있고, shout은 이름을 붙여야만 넘길 수 있다."""
    text = f"{greeting}, {name}님"
    return text.upper() + "!" if shout else text


print(greet("지민"))
print(greet("지민", "반갑습니다"))
print(greet("jimin", greeting="hello", shout=True))


def total(*numbers, **options):
    """*numbers는 튜블, **options는 dict로 들어온다."""
    result = sum(numbers)
    if options.get("double"):
        result *= 2
    return result


print(total(1, 2, 3))
print(total(1, 2, 3, double=True))


# 함정: 가변 기본 인자
def add_bad(item, bucket=[]):  # noqa: B006 (일부러 틀리게 쓴 예)
    bucket.append(item)
    return bucket


def add_good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(add_bad("a"), add_bad("b"))  # 같은 리스트를 공유한다
print(add_good("a"), add_good("b"))
