# Бот-секретарь

Мой первый pet-проект. Бот написан с помощью библиотеки aiogram. Включает весь неоходимый функционал, а именно:

* inline-клавиатуры( https://github.com/sergeykolbasin97/MyFirstBot/blob/master/keyboards/inline_keyboards.py)
* reply-клавиатуры (https://github.com/sergeykolbasin97/MyFirstBot/blob/master/keyboards/reply_keyboards.py)
* работа с различными сценариями (https://github.com/sergeykolbasin97/MyFirstBot/tree/master/states)
* настроенная админка (https://github.com/sergeykolbasin97/MyFirstBot/blob/master/admin.py)
* подключение к БД
* проверка на мат (https://github.com/sergeykolbasin97/MyFirstBot/blob/master/handlers/swear.py)
* хендлеры на конкретный ответ (https://github.com/sergeykolbasin97/MyFirstBot/tree/master/handlers/custom_handlers)
* отправление клиентом геолокации и личного номере телефона (https://github.com/sergeykolbasin97/MyFirstBot/blob/master/keyboards/reply_keyboards.py)

## Как запустить проект

1. В Telegram-боте **BotFather** необходимо получить токен бота
2. Создать папку *.env* и внесту туда токен, который сгенерировал **BotFather**
3. Установить все необходимые расширения из файла *requirements.txt* 
4. Скачать все папки и файлы из репозитория 
5. Запустить проект через *run.py*

## Архитектура проекта 

* *database* - папка для работы с базой
* *handlers* - папка с реакциями бота на запросы клиента
* *keyboards* - папка с кнопками(клавиатурой) бота
* *states* - папка с состояниями бота 
* *utils* - папка с функциями проверки корректности ввода клиентом и проверкой на мат
* *loader.py* - файл с инициализацией самого бота и окружения
* *run.py* - файл, запускающий бота 
* *requirements.txt* - текстовый файл с необходимыми расширениями
* *admin.py* - файл с админкой

## Применение алгоритмов в проекте

Для того, чтобы продемонстрировать знания основ программирования и синтаксиса языка Python, внес в проект несколько функций

### 1. 
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
- работы с списками, словарями
- работы с условным оператором
- работы с циклом for
- работы с модулем datetime

## Библиотеки 
```
aiogram==2.25.1
aiohttp==3.8.4
aiosignal==1.3.1
async-timeout==4.0.2
attrs==23.1.0
Babel==2.9.1
certifi==2022.12.7
charset-normalizer==3.1.0
emoji==2.2.0
frozenlist==1.3.3
idna==3.4
magic-filter==1.0.9
multidict==6.0.4
python-dateutil==2.8.2
python-dotenv==1.0.0
pytz==2023.3
six==1.16.0
yarl==1.9.2
```
====
## Язык проекта 
Python 
