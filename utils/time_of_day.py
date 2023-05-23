from datetime import datetime
import pytz

def check_daytime():
    tz = pytz.timezone('Europe/Moscow')
    curr_hour = datetime.now(tz).time().hour
    if curr_hour in range(10, 16):
        return 'Хорошего дня!'
    elif curr_hour in range(17, 22):
        return 'Хорошего вечера!'
    else:
        return 'Доброй ночи!'


