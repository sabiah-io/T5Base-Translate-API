from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    VERSION: str = "0.1.0"
    RELEASE_ID: str = "0.1.0"
    TITLE: str = "T5-Base Translation API"

    class Config:
        case_sensitive = True


# initialize Settings class
settings = Settings()
