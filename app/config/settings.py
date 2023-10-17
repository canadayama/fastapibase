"""
    config.settings.py
"""
from pydantic_settings import BaseSettings, SecretStr, SettingsConfigDict


class Settings(BaseSettings):
    db_dialect: str = "mysql"
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str = ""
    db_username: str = ""
    db_password: SecretStr = ""

    model_config = SettingsConfigDict(
                        case_sensitive = False,
                        env_prefix = '',
                        env_file = '.env',
                        env_file_encoding = 'utf-8',
                        #secrets_dir = '.secrets',
                    )