# import os
# from dotenv import load_dotenv

# load_dotenv()

# APP_NAME = os.getenv("APP_NAME")
# DEBUG_MODEL = os.getenv("DEBUG_MODEL") == "True"
# DATABSE_URL = os.getenv("DATABASE_URL")
# SECRET_KEY = os.getenv("SECRET_KEY")

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    DEBUG_MODEL: bool
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()

