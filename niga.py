import asyncio

import aiogram as aiogram
import logging
from aiogram import Bot, Dispatcher, executor, filters, types

API_TOKEN = '' #твйо токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет!\nЯ существую для того, чтобы ты изучал Python!\nКак тебя зовут?")

@dp.message_handler(regexp="(^Давид| Иван | Ваня)")
async def cats(message: types.Message):
    with open('gun.png', 'rb') as photo:

        await message.reply_photo(photo, caption=' Закрывай игры.')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Очень приятно, "+message.text)

    await message.reply("Хочешь увидеть смешные картинки? A я все равно покажу.")
    await asyncio.sleep(2)
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile("pic1.png"), "Картинка!")
    media.attach_photo(types.InputFile("pic2.png"), "Больке картинок!")
    media.attach_photo(types.InputFile("pic3.png"), "Mem,")

    await message.reply_media_group(media = media)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
