import sqlite3 as sql3

def sql_new_base():
    global base, cur
    base = sql3.connect('new_base.db')
    cur = base.cursor()
    if base:
        print(f'База данных {base} успешно подключена!')
        pass