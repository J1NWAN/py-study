# list : Java의 ArrayList와 비슷한 자료구조
langs = ["java", "python", "go", "rust"]
langs.append("Kotlin")  # 리스트에 요소 추가
print(langs[0], langs[-1])
print(langs[1:3])

# dict: Java의 HashMap
ports = {"http": 80, "https": 443, "ftp": 21}
ports["ssh"] = 22
for name, port in ports.items():
    print(f"{name} > {port}")

# set, tuple
seen = ["INFO", "ERROR", "INFO"]
levels = set(seen)
point = (3, 4)
x, y = point
print(levels, x + y)

# 컴프리헨션: Java의 stream.filter().map().toList()
lengths = [len(s) for s in langs if s != "go"]
print(lengths)
print(len("Python"))

items = []
if not items:
    print("비어 있음")
