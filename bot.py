from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os

TOKEN = "ضع_التوكن_هنا"
OWNER_ID = 5790968225  # ضع الايدي هنا

logging.basicConfig(level=logging.INFO)

def start(update, context):
    update.message.reply_text("👋 البوت شغال!")

def echo(update, context):
    if update.message.from_user.id == OWNER_ID:
        update.message.reply_text(f"✔️ وصلت رسالتك: {update.message.text}")
    else:
        update.message.reply_text("❌ انت مش المالك")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()
updater.idle()
