from pydantic import BaseSettings


class Settings(BaseSettings):
    BLOB_READ_WRITE_TOKEN: str

    class Config:
        env_file = ".env"


settings = Settings()
