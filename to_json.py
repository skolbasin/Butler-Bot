import json

swear_least = []

with open('swear_words.txt', 'r', encoding='utf-8') as file:
    for i_string in file:
        swear_word = i_string.lower().split('\n')[0]
        if swear_word != '':
            swear_least.append(swear_word)

with open('swear_words.json', 'w', encoding='utf-8') as file_2:
    json.dump(swear_least, file_2)