from fastapi import FastAPI, HTTPException
from app.config import settings
from app.models import TelegramUpdate, BotResponse
from app.services.bot_core import handle_incoming_text

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.get("/")
def index():
    return {"bot": settings.PROJECT_NAME, "status": "online"}

@app.post("/telegram-webhook", response_model=BotResponse)
def webhook(update: TelegramUpdate):
    if not update.message or "chat" not in update.message:
        raise HTTPException(status_code=400, detail="Invalid message payload")
    chat_id = update.message["chat"]["id"]
    text = update.message.get("text", "")
    reply = handle_incoming_text(chat_id, text)
    return BotResponse(chat_id=chat_id, text=reply)
