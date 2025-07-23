from fastapi import FastAPI, Request
import telegram
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)
app = FastAPI()

@app.post("/")
async def webhook(request: Request):
    data = await request.json()
    message = data.get("message")
    if message:
        chat_id = message["chat"]["id"]
        text = message.get("text", "")
        bot.send_message(chat_id=chat_id, text="✅ تم استلام رسالتك بنجاح.")
    return {"ok": True}