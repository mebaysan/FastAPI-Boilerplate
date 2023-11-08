from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class LoggingSettings(BaseSettings):
    log_level: str = "INFO"
    log_to_file: bool = False
    log_to_console: bool = True
    log_file_path: str = "my_app.log"


class AppSettings(BaseSettings):
    app_name: str = "My App"


logging_settings = LoggingSettings()
app_settings = AppSettings()
