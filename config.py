import dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOGIN: str
    PASSWORD: str
    browserstack_url: str = 'http://hub.browserstack.com/wd/hub'
    app_url: str = 'bs://sample.app'
    project_name: str = 'First Python Mobile'
    build_name: str = 'browserstack-build-1'
    session_name: str = 'Browserstack first_test'
    android_version: str = '9.0'
    android_device: str = 'Google Pixel 3'
    android_platform: str = 'android'


settings = Settings(_env_file=dotenv.find_dotenv(), _env_file_encoding='utf-8')
