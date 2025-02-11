from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from payments import send_payment_invoice
from subscription import check_subscription

async def start(update: Update, context: CallbackContext):
    """Handles /start command"""
    user_id = update.message.from_user.id

    if await check_subscription(user_id):
        await update.message.reply_text("✅ You are already in the channel! Special giveaways coming soon.")
        return

    keyboard = [[InlineKeyboardButton("💳 Pay 5 Telegram Stars", callback_data="pay_5_stars")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("💰 Pay total 15 Telegram Stars to join the channel.\n"
                                    "💳 Pay 5 stars advance now.", reply_markup=reply_markup)

async def handle_payment(update: Update, context: CallbackContext):
    """Initiates payment for 5 Telegram Stars"""
    await send_payment_invoice(update, context, 5)
