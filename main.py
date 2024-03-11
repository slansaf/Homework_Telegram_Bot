import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import kb1, kb2
from random_fox import fox

#подключение логгирование
logging.basicConfig(level=logging.INFO)

# создаем объект бота
bot = Bot(token=config.token)

#Диспечер
dispecher = Dispatcher()

#Хендлер на команду /start
@dispecher.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)

#Хендлер на команду /stop
@dispecher.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')

#Хендлейр на команду  /fox
@dispecher.message(Command('fox'))
@dispecher.message(Command('лиса'))
@dispecher.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
    #await bot.send_photo(message.from_user.id, photo=img_fox)

#Хендлер на собщения
@dispecher.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет - {name}')
    elif 'пока' in msg_user:
        await message.answer(f'Пока - {name}')
    elif 'ты кто' in msg_user:
        await message.answer_dice(emoji="")
    elif 'лису' in msg_user:
        await message.answer(f'Смотри у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова!')
    await message.answer(f'Ты написал - {msg_user}')

async def main():
    await dispecher.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
