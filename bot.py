import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename = "bot.log", level=logging.INFO)

PROXY = {"proxy_url":settings.PROXY_URL, "urllib3_proxy_kwargs": {"username": settings.PROXY_NAME, "password": settings.PROXY_PASSWORD}}

def user_hello(update, context):
    print("Вызвана команда /start")
    update.message.reply_text("Здравствуй, пользователь!")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater("2108202034:AAEcRWJKD_laDX13XDydpBaiEpGlfBKlIr8", use_context=True) 

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", user_hello))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("BOT STARTED!")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()


