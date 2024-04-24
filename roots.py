import sqlite3


class Database:
    def __init__(self, database):
        self.database = database

    def Connection(self):
        conn = sqlite3.connect(self.database)
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS users (id auto_increment primary key, name varchar(50), name_id varchar(50))''')
        conn.commit()
        cur.close()
        conn.close()

    def EndOfTask(self, message):
        conn = sqlite3.connect(self.database)
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO users (name) VALUES (?)', (message.from_user.first_name,))
        conn.commit()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        info = ''
        for el in users:
            info += f'Name: {el[1]}'
        cur.close()
        conn.close()
        return info

    def Result(self, message):
        print('Вы скуф')
