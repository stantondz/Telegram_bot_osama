import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# نجيب المتغيرات من Render Environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) == str(USER_ID):
        await update.message.reply_text("✅ البوت شغال عندك يا صاحبي!")
    else:
        await update.message.reply_text("⛔ معندكش صلاحية تستعمل هذا البوت.")

# أمر /ping
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! البوت حي 🎉")

def main():
    # نربط البوت بالتوكن
    app = Application.builder().token(BOT_TOKEN).build()

    # نضيف الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))

    # نشغل البوت
    print("🚀 البوت بدأ يشتغل...")
    app.run_polling()

if __name__ == "__main__":
    main()
