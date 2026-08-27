from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    market_provider: str = "deriv"
    market_api_url: str = ""
    market_api_token: str = ""
    gemini_api_key: str = ""
    news_api_key: str = ""
    telegram_bot_token: str = ""
    telegram_chat_id: str = ""
    a_plus_threshold: int = 92
    min_rr: float = 2.0
    stale_seconds: int = 15

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
