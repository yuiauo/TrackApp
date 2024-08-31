from pydantic_settings import BaseSettings


class DbSettings(BaseSettings):

    PORT: str
    HOST: str
    DATABASE: str
    USER: str
    PASSWORD: str

    class Config:
        env_file = ".env"

