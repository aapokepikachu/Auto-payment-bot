import os
import threading
from flask import Flask
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, PreCheckoutQueryHandler, MessageHandler, filters

from bot.handlers import start, handle_payment
from bot.payments import send_payment_invoice
from bot.subscription import check_subscription
from bot.config import BOT_TOKEN

# Initialize Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Function to run the Telegram bot
def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_5_stars$"))
    application.add_handler(PreCheckoutQueryHandler(send_payment_invoice))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, send_payment_invoice))

    application.run_polling()

# Run Flask and the bot together
if __name__ == "__main__":
    # Start the Telegram bot in a separate thread
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Start Flask server
    port = int(os.environ.get("PORT", 8080))  # Render's assigned PORT
    app.run(host="0.0.0.0", port=port)
