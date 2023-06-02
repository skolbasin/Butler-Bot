import sqlite3 as sql3

def sql_new_base():
    global base, cur
    base = sql3.connect('req_base.db')
    cur = base.cursor()
    if base:
        print(f'База данных {base} успешно подключена!')
    base.execute('CREATE TABLE IF NOT EXISTS {}'
                 '(req_id INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'user_name VARCHAR(25), '
                 'req_type TEXT, '
                 'description TEXT, '
                 'created_at DATETIME, '
                 'implementation TEXT) '.format('requests')
                 )
    base.commit()

    # если понадобится сформировать заявку вручную
    # cur.execute('INSERT INTO requests VALUES(?, ?)', ('Иван', 'Другое', 'Хочу...', '2023-05-23 12:12:34'))
    # base.commit()
# async def add_request(state):
#     cur.execute('INSERT INTO requests VALUES (?, ?, ?, ?)', tuple(data.values()))
#     base.commit()

async def db_table_val(user_name: str, req_type, description, created_at, implementation):
	cur.execute('INSERT INTO requests (user_name, req_type, description, created_at, implementation ) VALUES (?, ?, ?, ?, ?)', (user_name, req_type, description, created_at, implementation))
	base.commit()

async def check_db(message):
    count = 1
    for i_elem in cur.execute('SELECT * FROM requests').fetchall():
        await message.answer(f'<b>Заявка {count}</b>\n'
                             f'<u>ID</u>: {i_elem[0]}\n'
                             f'<u>Имя</u>: {i_elem[1]}\n'
                             f'<u>Тип</u>: {i_elem[2]}\n'
                             f'<u>Описание</u>: {i_elem[3]}\n'
                             f'<u>Создана</u>: {i_elem[4][:16]}\n'
                             f'<u>Статус</u>: {i_elem[5]}',
                             parse_mode='html')
        count += 1

async def read_db():
    return cur.execute('SELECT * FROM requests').fetchall()

async def delete_db(data):
    cur.execute('DELETE FROM requests WHERE req_id == ?', (data,))
    base.commit()

async def change_db_status(data):
    cur.execute('UPDATE requests SET implementation="Обработано" WHERE req_id == ?', (data,))
    base.commit()
