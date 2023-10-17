"""
    config.settings.py
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str = ""

    model_config = SettingsConfigDict(
                        case_sensitive = False,
                        env_prefix = '',
                        env_file = '.env',
                        env_file_encoding = 'utf-8',
                        #secrets_dir = '.secrets',
                    )