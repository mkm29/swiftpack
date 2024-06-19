"""Settings module for the application, loads settings from .env file."""

# from pydantic import BaseSettings
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "swiftpack"
    # Database settings
    database_type: str
    database_user: str
    database_password: str
    database_host: str
    database_port: int
    # API settings
    api_prefix: str = "/v1/api"
    # Logging settings
    log_level: str = "DEBUG"
    # Testing settings
    test_database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

    @property
    def database_url(self):
        db_protocol: str = None
        if self.database_type == "postgres":
            db_protocol = "postgresql+asyncpg"
        elif self.database_type == "sqlite":
            db_protocol = "sqlite"
        return (
            f"{db_protocol}://{self.database_user}:{self.database_password}@{self.database_host}:{self.database_port}"
        )
