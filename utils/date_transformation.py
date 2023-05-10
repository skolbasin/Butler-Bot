# функция меняет стандартный формат datetime

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