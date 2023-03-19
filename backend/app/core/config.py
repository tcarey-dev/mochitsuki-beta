from typing import List
from pydantic import BaseSettings, AnyHttpUrl
from decouple import config


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRATION = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Mochitsuki"
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)
    OPENAI_KEY: str = config("OPENAI_KEY", cast=str)
    MOCHI_KEY: str = config("MOCHI_KEY", cast=str)

    class Config:
        case_sensitive = True


settings = Settings()
