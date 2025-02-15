from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./shortener.db"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379

settings = Settings()
