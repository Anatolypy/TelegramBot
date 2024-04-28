import random

import telebot
import os
import roots
from dotenv import load_dotenv
import answers

load_dotenv('bot_config/token.env')

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
c = []
answ1 = None
answ2 = None
answ3 = None
answ4 = None
answ5 = None
sigma = None
num = 0
questions_list = []

with open('phrases.txt', encoding='utf-8') as questions:
    read_questions = questions.read()
    questions_list.append(read_questions.split("\n"))
print(questions_list)

database = roots.Database(os.getenv('sql_name'))
database.Connection()


@bot.message_handler(commands=['start', 'help'])
def main(message):
    btn_yes = telebot.types.InlineKeyboardButton('Да', callback_data='answer_yes')
    btn_no = telebot.types.InlineKeyboardButton('Нет', callback_data='answer_no')
    keyboard_select = telebot.types.InlineKeyboardMarkup()
    keyboard_select.add(btn_yes, btn_no)

    if (message.from_user.last_name is not None):
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')
    else:
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')
    bot.send_message(message.chat.id, questions_list[0][0], reply_markup=keyboard_select)


@bot.callback_query_handler(func=lambda call: call.data == 'answer_yes')
def next_up(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Поехали!",
                          reply_markup=None)
    test1(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'answer_no')
def down_up(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Ладно, в следующий раз ;(", reply_markup=None)


def test1(message):
    btn1 = telebot.types.KeyboardButton('Мясо')
    btn2 = telebot.types.KeyboardButton('Рыба')
    btn3 = telebot.types.KeyboardButton('Морепродукты')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_message(message.chat.id, "И так начнём, первый вопрос.")
    bot.send_photo(message.chat.id, photo="https://i.artfile.ru/3000x2000_811359_%5Bwww.ArtFile.ru%5D.jpg",
                   caption=questions_list[0][2], reply_markup=markup)

    bot.register_next_step_handler(message, test2)


def test2(message):
    btn1 = telebot.types.KeyboardButton('Постоянно')
    btn2 = telebot.types.KeyboardButton('Не люблю')
    btn3 = telebot.types.KeyboardButton('Когда время есть')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_photo(message.chat.id,
                   photo="https://thenewsgod.com/wp-content/uploads/2021/08/load-image-2021-08-01T115912.108.jpeg",
                   caption=questions_list[0][3], reply_markup=markup)
    bot.register_next_step_handler(message, test3)
    global answ1
    answ1 = message.text


def test3(message):
    btn1 = telebot.types.KeyboardButton('Кошки')
    btn2 = telebot.types.KeyboardButton('Собаки')
    btn3 = telebot.types.KeyboardButton('Другое')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_photo(message.chat.id, photo="https://a-z-animals.com/media/2022/05/Best-dog-allergy-tests-header.jpg",
                   caption=questions_list[0][4], reply_markup=markup)
    bot.register_next_step_handler(message, test4)
    global answ2
    answ2 = message.text


def test4(message):
    btn1 = telebot.types.KeyboardButton('Костюм')
    btn2 = telebot.types.KeyboardButton('Джинсовая куртка')
    btn3 = telebot.types.KeyboardButton('Другое')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_photo(message.chat.id,
                   photo="https://ratatum.com/wp-content/uploads/2017/08/1429737953_smart-kezhual-2.jpg",
                   caption=questions_list[0][5], reply_markup=markup)
    bot.register_next_step_handler(message, test5)
    global answ3
    answ3 = message.text


def test5(message):
    btn1 = telebot.types.KeyboardButton('Читаю')
    btn2 = telebot.types.KeyboardButton('Играю в компьютерные игры')
    btn3 = telebot.types.KeyboardButton('Гуляю')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_photo(message.chat.id,
                   photo="https://www.factroom.ru/wp-content/uploads/2015/04/Depositphotos_30671459_m.jpg",
                   caption=questions_list[0][6], reply_markup=markup)
    bot.register_next_step_handler(message, end)
    global answ4
    answ4 = message.text


def end(message):
    last_info = database.EndOfTask(message)
    global answ5
    answ5 = message.text
    global sigma
    global num
    a = answers.question1[answ1]
    a2 = answers.question2[answ2]
    a3 = answers.question3[answ3]
    a4 = answers.question4[answ4]
    a5 = answers.question5[answ5]
    summa = (a + a2 + a3 + a4 + a5) // 15
    if 0 < summa <= 10:
        num = 1
        sigma = random.choice(answers.group1)
    elif 10 < summa <= 20:
        num = 2
        sigma = random.choice(answers.group2)
    else:
        num = 3
        sigma = random.choice(answers.group3)
    bot.send_photo(message.chat.id,
                   photo=answers.sigmas[num][sigma],
                   caption=f"Поздравляю! Вы <b>{sigma}</b>!", parse_mode="HTML")
    bot.send_message(message.chat.id, "Люди которые прошли тест")
    bot.send_message(message.chat.id, last_info)


if __name__ == '__main__':
    bot.infinity_polling()
