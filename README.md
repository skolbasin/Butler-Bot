# Бот-секретарь

Мой первый pet-проект. Бот написан с помощью библиотеки aiogram. Включает весь неоходимый функционал, а именно:

* inline-клавиатуры( https://github.com/sergeykolbasin97/MyFirstBot/blob/master/keyboards/inline_keyboards.py)
* reply-клавиатуры (https://github.com/sergeykolbasin97/MyFirstBot/blob/master/keyboards/reply_keyboards.py)
* работа с различными сценариями (https://github.com/sergeykolbasin97/MyFirstBot/tree/master/states)
* админка (https://github.com/sergeykolbasin97/MyFirstBot/blob/master/admin.py)
* работа с БД (https://github.com/sergeykolbasin97/Butler-Bot/tree/master/database)
* проверка на мат (https://github.com/sergeykolbasin97/MyFirstBot/blob/master/handlers/swear.py)
* обработчики команд (хендлеры)(https://github.com/sergeykolbasin97/Butler-Bot/tree/master/handlers)
* отправление клиентом геолокации и личного номере телефона (https://github.com/sergeykolbasin97/MyFirstBot/blob/master/keyboards/reply_keyboards.py)

## Как запустить проект

1. В Telegram-боте **BotFather** необходимо получить токен бота
2. Создать папку *.env* и внесту туда токен, который сгенерировал **BotFather**
3. Установить все необходимые расширения из файла *requirements.txt* 
4. Скачать все папки и файлы из репозитория 
5. Запустить проект через *run.py*
P.S. БД создается автоматически после первого запуска бота

## Архитектура проекта 

* *database* - папка для работы с базой
* *handlers* - папка с реакциями бота на запросы пользователя/администратора
* *keyboards* - папка с кнопками(клавиатурой) бота
* *states* - папка с состояниями бота 
* *utils* - папка с функциями проверки корректности ввода клиентом и проверкой на мат
* *loader.py* - файл с инициализацией самого бота, его окружения и меню команд
* *run.py* - файл, запускающий бота 
* *requirements.txt* - текстовый файл с необходимыми расширениями
* *admin.py* - файл с админкой

## Админка
В файле *admin.py* прописан хендлер на проверку администартором группы пользователя. После выполнения данной команды, в переменную **ID** сохраняется
ID администратора и ряд команд сможет совершать только он. В данном проекте почти все команды в открытом доступе, кроме проверки поступивших заявок от пользователей
```
@Mr_Butler.message_handler(commands='Заявки')
async def all_requests(message: types.message):
    if message.from_user.id == ID:
        await check_db(message)
```
Сама функция, выдающая результат из БД:
```
async def check_db(message):
    count = 1
    for i_elem in cur.execute('SELECT * FROM requests').fetchall():
        await message.answer(f'<b>Заявка {count}</b>\n'
                             f'<u>ID</u>: {i_elem[0]}\n'
                             f'<u>Имя</u>: {i_elem[1]}\n'
                             f'<u>Тип</u>: {i_elem[2]}\n'
                             f'<u>Описание</u>: {i_elem[3]}\n'
                             f'<u>Создана</u>: {i_elem[4][:16]}', 
                             parse_mode='html')
        count += 1
```
Но если Вы захотите прописать валидацию и к другим хендлерам, то необходимо в хендлере прописать условие `if message.from_user.id == ID`, сделать импорт переменной **ID** и перенести хендлер в файл *admin.py*.

## Работа с БД
Связь с Базой Данных осуществляется через машину состояний, в которой пользователь оформляет заявку на одно из 4х действий:
1. Приглашение на встречу
2. Попросить набрать
3. Зашифровать послание на языке 'Присивесет'
4. Другое

Сама таблица состоит из 6 полей: 
1. req_id - является PRIMARY KEY С AUTO_INCREMENT
2. user_name - имя пользователя
3. req_type - тип заявки
4. created_at - дата создания заявки
5. description - описание, в зависимости от типа заявки
6. implementation - статус, меняется по запросу администратора


После окончания заполнения заявки, данные уходят в БД, которая написана через SQLite.
Код машины - https://github.com/sergeykolbasin97/Butler-Bot/blob/master/handlers/states_handlers/add_request.py
Управлять БД может администратор. Он может посмотреть сами заявки:
```
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
```
изменить статус заявки с 'не обработано' на 'обработано'
```
async def change_db_status(data):
    cur.execute('UPDATE requests SET implementation="Обработано" WHERE req_id == ?', (data,))
    base.commit()

```
удалить заявку
```
async def delete_db(data):
    cur.execute('DELETE FROM requests WHERE req_id == ?', (data,))
    base.commit()
```
Удаление и изменение данные реализовано через inline-клавиатуру
```
@Mr_Butler.message_handler(commands='Редактировать')
async def all_requests(message: types.message):
    if message.from_user.id == ID:
        request_list = await read_db()
        count = 0
        for i_req in request_list:
            count += 1
            await bot.send_message(message.from_user.id, text=f'<b>Заявка {count}</b>\n{i_req}', reply_markup=inline_kb4, parse_mode='html')

inline_kb4 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Выполнено✅', callback_data='change1'),
                                                   InlineKeyboardButton(text='Удалить❌', callback_data='change2'))
```
## Применение алгоритмов в проекте

Для того, чтобы продемонстрировать знания основ программирования и синтаксиса языка Python, внес в проект несколько функций
* 1 ***Дешифровка языка 'Присивесет'***  

Суть шифра - после каждой гласной ставится буква 'c' и повторяется гласная.  
Пример: конь - косонь, рука -русукаса   
Данная функция принимает на вход зашифрованный текст и выдает расшифровку  
Сложность алгоритма - О(n)  
```
def translator(string: str):
  vowels = ['а', 'о', 'е', 'ё', 'и', 'ы', 'у', 'э', 'ю', 'я']
  new_list = list(string)
  for index, i_letter in enumerate(new_list):
    if i_letter in vowels:
      del new_list[index + 1:index + 3]
  return ''.join(new_list)
```

* 2 ***Функции***
  + 1.1. Функция меняет стандартный формат datetime 'YYYY-MM-DD'
  ```
  months_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
                 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

  end_ya = [1, 2, 4, 5, 6, 7, 9, 10, 11, 12]
  end_a = [3, 8]

  def transformation_date(date: str) -> str:
      list_format = date.split('-')
      if list_format[2][0] == '0':
          day = list_format[2][1]
      else:
          day = list_format[2]

      if list_format[1][0] == '0':
          month = int(list_format[1][1])
      else:
          month = int(list_format[1])

      for i, i_month in months_dict.items():
          if i == month and i in end_ya:
              month = i_month[:-1] + 'я'
              break
          elif i == month and i in end_a:
              month = i_month + 'а'

      year = list_format[0]
      return f'{day} {month} {year} г.'
  ```

      Данная функция демонстрирует знания: 
      - работы со списками, словарями
      - работы с условным оператором if
      - работы с циклом for
      - работы с модулем datetime
  
  
  Можно было сделать короче, используя сразу родительный падеж в словарях 
  
  
  
  + 1.2 Функция меняет окончание слова 'день' в зависимости от числа 
  ```
  list_1 = ['1']
  list_2 = ['2', '3', '4']
  list_3 = ['0', '5', '6', '7', '8', '9']

  def day_transformation(number: int) -> str:
    if str(number)[-1:] in list_1:
      return f'{str(number)} день'
    elif str(number)[-1:] in list_2:
      return f'{str(number)} дня'
    elif str(number)[-1:] in list_3:
      return f'{str(number)} дней'
  ```


## Библиотеки 

* aiogram==2.25.1
* aiohttp==3.8.4
* aiosignal==1.3.1
* async-timeout==4.0.2
* attrs==23.1.0
* Babel==2.9.1
* certifi==2022.12.7
* charset-normalizer==3.1.0
* emoji==2.2.0
* frozenlist==1.3.3
* idna==3.4
* magic-filter==1.0.9
* multidict==6.0.4
* python-dateutil==2.8.2
* python-dotenv==1.0.0
* pytz==2023.3
* six==1.16.0
* yarl==1.9.2

## Язык проекта 
Python 
