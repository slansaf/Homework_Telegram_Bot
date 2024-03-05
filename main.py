import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random

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
    await message.answer(f'Привет, {name}')

#Хендлер на команду /stop
@dispecher.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')

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
        await message.answer(f'Я бот - {name}')
    else:
        await message.answer(f'Я не знаю такого слова!')
    await  message.answer(f'Ты написал - {msg_user}')

async def main():
    await dispecher.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
