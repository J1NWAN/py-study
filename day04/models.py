from pydantic import BaseModel, Field


class DbConfig(BaseModel):
    path: str
    timeout_seconds: int = 3


class AppConfig(BaseModel):
    name: str
    port: int = Field(default=8000, ge=1, le=65535)
    debug: bool = False
    allowed_hosts: list[str] = []
    admin_email: str | None = None
    db: DbConfig
