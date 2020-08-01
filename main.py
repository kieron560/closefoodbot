import telegram
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


updater = Updater(token='1360339621:AAF86KnP2USNbPE5tP2IsPECIGuT0Q-sGbQ', use_context=True)
bot = telegram.Bot(token='1360339621:AAF86KnP2USNbPE5tP2IsPECIGuT0Q-sGbQ')

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)



updater.start_polling()

updater.stop()
