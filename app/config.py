from pydantic import BaseSettings


class Settings(BaseSettings):
    BLOB_READ_WRITE_TOKEN: str
    DEFAULT_FONT_URL: str

    MOCKUP_TENT_HALF_WALLS_FRONT: str
    MOCKUP_TENT_FULL_WALLS_FRONT: str
    MOCKUP_TENT_FULL_WALLS_SIDE: str
    MOCKUP_TENT_HALF_WALLS_SIDE: str
    MOCKUP_TENT_NO_WALLS: str
    MOCKUP_TENT_TOP_VIEW: str

    MOCKUP_ADD_ON_TABLE: str

    class Config:
        env_file = ".env"


settings = Settings()
