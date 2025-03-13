from pydantic import BaseSettings


class Settings(BaseSettings):
    VERCEL_BLOB_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
