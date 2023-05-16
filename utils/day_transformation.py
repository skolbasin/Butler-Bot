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
