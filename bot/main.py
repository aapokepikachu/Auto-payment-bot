import os
import threading
import asyncio
from flask import Flask
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, PreCheckoutQueryHandler, MessageHandler, filters
import logging

from bot.handlers import start, handle_payment
from bot.payments import send_payment_invoice
from bot.subscription import check_subscription
from bot.config import BOT_TOKEN

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Initialize Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Function to run the Telegram bot
async def run_bot():
    try:
        logger.info("Starting Telegram bot...")
        application = Application.builder().token(BOT_TOKEN).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_5_stars$"))
        application.add_handler(PreCheckoutQueryHandler(send_payment_invoice))
        application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, send_payment_invoice))

        await application.run_polling()
    except Exception as e:
        logger.error(f"Error starting bot: {e}")

def start_bot():
    asyncio.run(run_bot())

# Run Flask and the bot together
if __name__ == "__main__":
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()

    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Starting Flask server on port {port}...")
    app.run(host="0.0.0.0", port=port)
