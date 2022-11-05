from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    """Base settings."""
    class Config:
        env_file = '/code/app/config/.env'


class CommonSettings(Settings):
    """Common settings."""
    MONGODB_URL: str
    MONGODB_DB_NAME: str
    MAX_CONNECTIONS_COUNT: int
    MIN_CONNECTIONS_COUNT: int

    CLIENT_ORIGIN: str


class AuthSettings(Settings):
    """Authorization settings."""
    JWT_ALGORITHM: str
    JWT_ACESS_TOKEN_COOKIE_KEY: str = 'access_token'
    JWT_REFRESH_COOKIE_KEY: str = 'refresh_token'
    JWT_ACCESS_TOKEN_EXPIRE: int
    JWT_REFRESH_TOKEN_EXPIRE: int
    JWT_SECRET_KEY: str
    JWT_REFRESH_SECRET_KEY: str


class EmailSettings(Settings):
    """Email settings."""
    MAIL_SERVER: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_PORT: int
    MAIL_FROM: EmailStr
    MAIL_TLS: bool = True
    MAIL_SSL: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True


common_settings = CommonSettings()
auth_settings = AuthSettings()
email_settings = EmailSettings()
