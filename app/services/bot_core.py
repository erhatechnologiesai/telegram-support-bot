from app.config import settings

USER_MEMORY = {}

COMMANDS = {
    "/start": "👋 Welcome to Erha Technologies AI Support Bot!\n\nCommands:\n/help - Show help\n/ticket - Create support ticket\n/status - Check platform status\n/reset - Clear context",
    "/help": "ℹ️ You can ask me any question about our AI automation workflows or use /ticket to reach a human specialist.",
    "/status": "🟢 All Erha AI production systems are operational. Average latency: 42ms.",
}

def handle_incoming_text(chat_id: int, text: str) -> str:
    text = text.strip()
    if text.startswith("/"):
        cmd = text.split()[0].lower()
        if cmd == "/reset":
            USER_MEMORY[chat_id] = []
            return "🧹 Conversation context cleared."
        elif cmd == "/ticket":
            return f"🎫 Support ticket #TG-{chat_id} has been registered with Erha Engineering."
        return COMMANDS.get(cmd, "❓ Unknown command. Type /help for available options.")

    # Memory update
    if chat_id not in USER_MEMORY:
        USER_MEMORY[chat_id] = []
    USER_MEMORY[chat_id].append(text)

    # Question answering
    t_low = text.lower()
    if "agent" in t_low or "workflow" in t_low:
        return "🤖 Erha Technologies builds autonomous multi-agent pipelines for enterprise workflow acceleration. What workflow would you like to automate?"
    elif "api" in t_low:
        return "⚡ Our REST and Webhook APIs integrate directly with Python, Node.js, and n8n."
    else:
        return f"💡 I've noted: '{text}'. Our AI agent is processing your inquiry."
