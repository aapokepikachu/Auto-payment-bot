from telegram.ext import Application, CommandHandler, CallbackQueryHandler, PreCheckoutQueryHandler, MessageHandler, filters
from .handlers import start, handle_payment
from .payments import send_payment_invoice
from .subscription import check_subscription

from .config import BOT_TOKEN

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_5_stars$"))
    application.add_handler(PreCheckoutQueryHandler(send_payment_invoice))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, send_payment_invoice))

    application.run_polling()

if __name__ == "__main__":
    main()

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use Render’s PORT
    app.run(host="0.0.0.0", port=port)
