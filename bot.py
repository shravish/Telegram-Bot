from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TELEGRAM_TOKEN
from db import add_user
import scheduler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✈️ Welcome! Use this format to track flights:\n"
        "/track <FROM> <TO> <YYYY-MM-DD> <MAX_PRICE>\n"
        "Example:\n/track JFK LAX 2025-07-10 250"
    )

async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        origin, destination, date, price = context.args
        add_user(update.effective_chat.id, origin.upper(), destination.upper(), date, float(price))
        await update.message.reply_text(
            f"🔔 Tracking flight {origin.upper()} ➡ {destination.upper()} on {date} under ${price}"
        )
    except Exception:
        await update.message.reply_text("❗ Usage: /track JFK LAX 2025-07-10 250")

def alert_user(chat_id, price, user):
    text = (
        f"📉 Price drop alert!\n"
        f"{user['origin']} ➡ {user['destination']} on {user['date']} is now ${price}!"
    )
    app.bot.send_message(chat_id=chat_id, text=text)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("track", track))

if __name__ == "__main__":
    scheduler.start()
    app.run_polling()
