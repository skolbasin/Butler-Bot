
def translator(string: str):
  vowels = ['а', 'о', 'е', 'ё', 'и', 'ы', 'у', 'э', 'ю', 'я']
  new_list = list(string)
  for index, i_letter in enumerate(new_list):
    if i_letter.lower() in vowels:
      del new_list[index + 1:index + 3]
  return ''.join(new_list)