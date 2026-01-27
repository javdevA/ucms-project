from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./ucms.db"
    secret_key: str = "your-super-secret-key-change-in-prod"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

settings = Settings()
