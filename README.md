# Бот-секретарь

Мой первый pet-проект. Бот написан с помощью библиотеки aiogram. Включает весь неоходимый функционал, а именно:

* inline-клавиатуры 
* reply-клавиатуры
* работа по сценарию
* проверка на мат
* хендлеры на конкретный ответ
* отправление клиентом геолокации и личный номер телефона
* настроенная админка
* подключение к БД

## Как запустить проект

1. В Telegram-боте **BotFather** необходимо получить токен бота
2. Создать папку *.env* и внесту туда токен, который сгенерировал **BotFather**
3. Установить все необходимые расширения из файла *requirements.txt* 
4. Скачать все папки b файлы из репозитория 
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

## Язык проекта 
Python 
