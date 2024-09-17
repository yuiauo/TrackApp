from pydantic_settings import BaseSettings


class DbSettings(BaseSettings):

    PORT: str
    HOST: str
    DATABASE: str
    USERNAME: str
    PASSWORD: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"