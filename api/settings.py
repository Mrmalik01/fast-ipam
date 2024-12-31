from enum import Enum
import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    pool_table_name: str
    resource_allocation_table_name: str
    project_table_name: str
    project_table_gsi_project_name: str
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str
    env: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
