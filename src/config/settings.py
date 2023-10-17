"""
    config.settings.py
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str = ""

    model_config = SettingsConfigDict(env_file='.env')