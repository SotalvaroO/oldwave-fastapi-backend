
from typing import Optional
from dotenv import load_dotenv
import os
from pydantic import BaseSettings, Field

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, 'config.env'))

class Settings(BaseSettings):

    ENVIRONMENT: str = Field(None, env=os.getenv('MONGO_URL_DEV'))  # por default, 'env' is a environment var
    print(os.getenv('MONGO_URL_DEV'))
    VAR: Optional[str]

    class Config:
        env_file: str = "../config.env"


class DevSettings(Settings):
    class Config:
        env_prefix: str = "DEV_"


class ProdSettings(Settings):
    class Config:
        env_prefix: str = "PROD_"


def get_settings():
    if "prod" == Settings().ENVIRONMENT:
        return ProdSettings()
    else:
        return DevSettings()


config = get_settings()

#print(config.ENVIRONMENT)
#print(config.VAR)