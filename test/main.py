

#my token 
#1894220658:AAHYFIQKt9ytd7IqtqDbyik2Q7jXMjLTtNU

#general link

#https://api.telegram.org/bot1894220658:AAHYFIQKt9ytd7IqtqDbyik2Q7jXMjLTtNU/getMe
API_KEY = '1894220658:AAHYFIQKt9ytd7IqtqDbyik2Q7jXMjLTtNU'
#import Constants as keys
from telegram.ext import * 
import Responses as R

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type something random to get started')


def help_command(update, context):
    update.message.reply_text('Ask for help')
    

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print("error error {context.error}")

def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(1)

    updater.idle()



main()
