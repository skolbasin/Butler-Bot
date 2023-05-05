# фильтр мата
import json, string
from run import Mr_Butler, bot
from aiogram.types import message

@Mr_Butler.message_handler()
async def swear_check(message: message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('swear_words.json')))) != set():
        await bot.send_photo(message.from_user.id, photo=open('foto/best_of_the_best_JK.jpg', 'rb'),
                             caption='К сожалению, меня так воспитали, что я не воспринимаю любую ненормативную лексику🙅‍♂️\n'
                                     'Придется Вам подумать как объяснить мне по другому🖤')
        await message.delete()