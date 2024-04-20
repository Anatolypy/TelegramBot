from telegram.ext import Application, CommandHandler
from telegram import ReplyKeyboardMarkup
import logging

BOT_TOKEN = '6979060436:AAF9J29cBCUadUi5dp2Dq7g1HUzr1CzdKtc'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

reply_keyboard = [['/help']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
file = open('phrases.txt', encoding='utf-8')


async def help(update, context):
    await update.message.reply_text(file.readlines()[1])


async def start(update, context):
    await update.message.reply_text(file.readlines()[0], reply_markup=markup)


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


if __name__ == '__main__':
    main()
