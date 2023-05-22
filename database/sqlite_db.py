import sqlite3 as sql3

def sql_new_base():
    global base, cur
    base = sql3.connect('req_base.db')
    cur = base.cursor()
    if base:
        print(f'База данных {base} успешно подключена!')
    base.execute('CREATE TABLE'
                 'IF NOT EXISTS {}'
                 '(req_id INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'user_name VARCHAR(25), '
                 'req_type TEXT, '
                 'description TEXT, '
                 'created_at DATETIME)'.format('requests')
                 )
    base.commit()

    # если понадобится сформировать заявку вручную
    # cur.execute('INSERT INTO requests VALUES(?, ?)', ('Иван', 'Другое', 'Хочу...', '2023-05-23 12:12:34'))
    # base.commit()
async def add_request(state):
    cur.execute('INSERT INTO requests VALUES (?, ?, ?, ?)', tuple(data.values()))
    base.commit()

