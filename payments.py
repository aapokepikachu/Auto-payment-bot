from telegram import Update, LabeledPrice
from telegram.ext import CallbackContext
from bot.config import PAYMENT_PROVIDER_TOKEN

async def send_payment_invoice(update: Update, context: CallbackContext, amount):
    """Sends a payment invoice"""
    user_id = update.callback_query.from_user.id
    title = "Payment"
    description = f"Pay {amount} Telegram Stars to proceed."
    payload = f"payment_{amount}_stars_{user_id}"
    currency = "USD"
    prices = [LabeledPrice(label=f"{amount} Telegram Stars", amount=amount * 100)]  # Convert to smallest unit

    await context.bot.send_invoice(
        chat_id=user_id, title=title, description=description,
        payload=payload, provider_token=PAYMENT_PROVIDER_TOKEN,
        currency=currency, prices=prices
    )
