import os
class Settings:
    PROJECT_NAME: str = "AI Telegram Support Bot"
    VERSION: str = "1.0.0"
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")
    ADMIN_CHAT_ID: str = os.getenv("ADMIN_CHAT_ID", "987654321")
    DEMO_MODE: bool = os.getenv("DEMO_MODE", "true").lower() == "true"
settings = Settings()
