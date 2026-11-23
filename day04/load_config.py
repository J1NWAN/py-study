from pathlib import Path

from models import AppConfig

text = Path("day04/config.json").read_text(encoding="utf-8")
config = AppConfig.model_validate_json(text)  # JSON 문자열 -> 검증된 객체

print(config.name, config.port, config.db.path)
print(type(config.port), config.admin_email)

# 객체 -> dict, JSON
print(config.model_dump()["db"])
print(config.model_dump_json(indent=2))
