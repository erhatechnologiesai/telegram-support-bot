from pydantic import BaseModel
from typing import Optional, Dict, Any

class TelegramUpdate(BaseModel):
    update_id: int
    message: Optional[Dict[str, Any]] = None

class BotResponse(BaseModel):
    chat_id: int
    text: str
    parse_mode: str = "Markdown"
