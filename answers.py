import telebot
from telebot import types

bot = telebot.TeleBot("YOUR_BOT_TOKEN")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item_yes = types.InlineKeyboardButton("Да", callback_data='yes_1')
    item_no = types.InlineKeyboardButton("Нет", callback_data='no_1')
    markup.add(item_yes, item_no)
    bot.send_message(message.chat.id, "Первый вопрос: Вы готовы начать?", reply_markup=markup)




bot.polling()
