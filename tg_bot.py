from typing import Final
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackContext
import logging


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a Telegram bot object
TOKEN: Final = 'BOT-TOKEN'
BOT_USERNAME: Final = '@BOTUN'

async def error_handler(update: object, context: CallbackContext) -> None:
    """Log the error and send a message to notify the developer."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

    # Notify the developer
    # You can replace 'DEVELOPER_CHAT_ID' with your actual chat ID
    await context.bot.send_message(chat_id='DEVELOPER_CHAT_ID', text=str(context.error))

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text=f"Your chat ID is {update.effective_chat.id}")

async def info_inline_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Button 1", url='http://example.com')],
        [InlineKeyboardButton("Button 2", url='http://example.com')],
        # Add more buttons here if necessary
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('This is the info message.', reply_markup=reply_markup)

async def info_keyboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("Button 1")],
        [KeyboardButton("Button 2")],
        # Add more buttons here if necessary
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text('This is the info message.', reply_markup=reply_markup)

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    start_handler = CommandHandler('start', start_command)
    app.add_handler(start_handler)

    info_handler = CommandHandler('info1', info_inline_command)
    app.add_handler(info_handler)
    info_handler = CommandHandler('info2', info_keyboard_command)
    app.add_handler(info_handler)

    # Error handler
    app.add_error_handler(error_handler)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
