import os
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Load bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Define a start command
def start(update, context):
    update.message.reply_text("Hello! I am your expense tracking bot. How can I help you?")

# Handle regular text messages
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Create Updater and pass it the bot's token
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command and message handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
