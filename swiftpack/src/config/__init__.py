"""Settings module for the application, loads settings from .env file."""

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = Field(default="Swiftpack", env="APP_NAME")
    # Database settings
    database_type: str = Field(env="DATABASE_TYPE")
    database_user: str = Field(env="DATABASE_USER")
    database_password: str = Field(env="DATABASE_PASSWORD")
    database_host: str = Field(default="localhost", env="DATABASE_HOST")
    database_name: str = Field(default="swiftpack", env="DATABASE_NAME")
    database_port: int = Field(default=5432, env="DATABASE_PORT")
    # API settings
    api_prefix: str = Field(default="/api/v1", env="API_PREFIX")
    # Logging settings
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    # Testing settings
    test_database_url: str = Field(default="sqlite:///./test.db", env="TEST_DATABASE_URL")

    class Config:
        env_file = ".env"
        extra = "ignore"
        # get my validate on...

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


# if __name__ == "__main__":
#     # import pprint
#     from pprint import pprint
#     settings = Settings()
#     pprint(settings.dict())
