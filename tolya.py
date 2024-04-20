import telebot
from telebot import types

bot = telebot.TeleBot('6979060436:AAF9J29cBCUadUi5dp2Dq7g1HUzr1CzdKtc')
file = open('phrases.txt', encoding='utf-8')
f = file.read()
newf = f.split("\n")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')
    bot.send_message(message.chat.id, newf[0])
    bot.register_next_step_handler(message, test)


def test(message):
    if message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Ну хорошо, до скорого')
    else:
        bot.send_photo(message.chat.id,
                       'https://thumbs.dreamstime.com/b/egg-roll-spring-roll-popiah-vietnamese-cuisine-thai-style-sweet-suace-wooden-table-71117155.jpg')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Я пока не могу помогать')


bot.polling(none_stop=True)
