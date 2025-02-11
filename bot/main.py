from telegram.ext import Application, CommandHandler, CallbackQueryHandler, PreCheckoutQueryHandler, MessageHandler, filters
from bot.handlers import start, handle_payment
from bot.payments import send_payment_invoice
from bot.subscription import check_subscription

from bot.config import BOT_TOKEN

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_payment, pattern="^pay_5_stars$"))
    application.add_handler(PreCheckoutQueryHandler(send_payment_invoice))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, send_payment_invoice))

    application.run_polling()

if __name__ == "__main__":
    main()
