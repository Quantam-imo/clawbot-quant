import os
import requests
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = os.getenv("CLAWBOT_API_URL", "http://localhost:8000/api/v1/clawbot/ask")

class TelegramBot:
    def __init__(self, token):
        self.bot = Bot(token)
        self.app = ApplicationBuilder().token(token).build()
        self.app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.handle_message))
        self.app.add_handler(CommandHandler("start", self.handle_start))

    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hi! I'm Clawbot. Ask me anything about trading or gold futures.")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_msg = update.message.text.strip()
        print(f"[TelegramBot] Received message: {user_msg}")
        payload = {"question": user_msg}
        try:
            resp = requests.post(API_URL, json=payload)
            reply = resp.json().get("reply", "Sorry, no response.")
            print(f"[TelegramBot] Reply: {reply}")
        except Exception as e:
            reply = f"Error: {str(e)}"
            print(f"[TelegramBot] Error: {e}")
        await update.message.reply_text(reply)

    def run(self):
        self.app.run_polling()

if __name__ == "__main__":
    if not TELEGRAM_TOKEN:
        print("TELEGRAM_BOT_TOKEN not set in environment.")
    else:
        TelegramBot(TELEGRAM_TOKEN).run()
