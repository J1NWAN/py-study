from pathlib import Path

from models import AppConfig
from pydantic import ValidationError

text = Path("day04/bad_config.json").read_text(encoding="utf-8")

try:
    AppConfig.model_validate_json(text)
except ValidationError as e:
    print(e)
