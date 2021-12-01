import logging
from aiogram import Bot, Dispatcher, types, executor
from Checkword import checkWord

APi_KEY = "2130848468:AAGXSibW1gHFcXi_5OOClb6Zkj9yI9RqAek"

#loggin Configure
logging.basicConfig(level=logging.INFO)

#bot and dispatcher
bot = Bot(token=APi_KEY)
dp = Dispatcher(bot)

#Commands
@dp.message_handler(commands=['start'])
async def begin(message:types.Message):
    await message.reply('Uz_imlo Botiga xush kelibsiz!')

@dp.message_handler(commands=['help'])
async def begin(message:types.Message):
    await message.reply("Botdan foydalanish uchun krill alifobsida so'z yuboring!")

@dp.message_handler()
async def checkImlo(message:types.Message):
    word = message.text
    result = checkWord(word)
    if result ['available']:
        response = f"✅{word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅{text.capitalize()}\n"
    await message.answer(response)


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)


