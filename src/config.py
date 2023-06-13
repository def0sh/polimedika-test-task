from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_TITLE = 'University management system'
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_NAME: str

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()
