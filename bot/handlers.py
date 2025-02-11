import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from .payments import send_payment_invoice
from .subscription import check_subscription

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext):
    """Handles /start command"""
    user_id = update.message.from_user.id
    logger.info(f"Received /start command from user ID: {user_id}")

    if await check_subscription(user_id):
        await update.message.reply_text("✅ You are already in the channel! Special giveaways coming soon.")
        return

    keyboard = [[InlineKeyboardButton("💳 Pay 5 Telegram Stars", callback_data="pay_5_stars")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("💰 Pay total 15 Telegram Stars to join the channel.\n"
                                    "💳 Pay 5 stars advance now.", reply_markup=reply_markup)