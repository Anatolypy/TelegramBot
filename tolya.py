import telebot
import sqlite3

bot = telebot.TeleBot('6979060436:AAF9J29cBCUadUi5dp2Dq7g1HUzr1CzdKtc')
file = open('phrases.txt', encoding='utf-8')
f = file.read()
newf = f.split("\n")

ans1 = None
ans2 = None
ans3 = None
ans4 = None
ans5 = None


@bot.message_handler(commands=['start'])
def main(message):
    conn = sqlite3.connect('tolya.sql')
    cur = conn.cursor()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS users (id auto_increment primary key, name varchar(50), name_id varchar(50))''')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')
    bot.send_message(message.chat.id, newf[0])
    bot.register_next_step_handler(message, test1)


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Ну хорошо, до скорого')
    else:
        bot.register_next_step_handler(message, test1)


def test1(message):
    btn1 = telebot.types.KeyboardButton('Мясо')
    btn2 = telebot.types.KeyboardButton('Рыба')
    btn3 = telebot.types.KeyboardButton('Морепродукты')
    btn4 = telebot.types.KeyboardButton('Другое')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_photo(message.chat.id, photo="https://i.artfile.ru/3000x2000_811359_%5Bwww.ArtFile.ru%5D.jpg",
                   caption=newf[2], reply_markup=markup)
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
                   caption=newf[3], reply_markup=markup)
    bot.register_next_step_handler(message, test3)


def test3(message):
    btn1 = telebot.types.KeyboardButton('Кошки')
    btn2 = telebot.types.KeyboardButton('Собаки')
    btn3 = telebot.types.KeyboardButton('Другое')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_photo(message.chat.id, photo="https://a-z-animals.com/media/2022/05/Best-dog-allergy-tests-header.jpg",
                   caption=newf[4], reply_markup=markup)
    bot.register_next_step_handler(message, test4)


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
                   caption=newf[5], reply_markup=markup)
    bot.register_next_step_handler(message, test5)


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
                   caption=newf[6], reply_markup=markup)
    bot.register_next_step_handler(message, end)


def end(message):
    conn = sqlite3.connect('tolya.sql')
    cur = conn.cursor()
    cur.execute(
        f'''INSERT INTO users (name, name_id) VALUES ('{message.from_user.first_name}', '{message.from_user.id}')''')
    conn.commit()
    cur.execute('''SELECT * FROM users''')
    users = cur.fetchall()
    info = f'Кто уже прошел тест:\n'
    for el in users:
        info += f'Name: {el[1]} ID: {el[2]}\n'
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Я пока не могу помогать')


bot.polling(none_stop=True)
