import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
from handlers import common, career_choice

async def main():
    # подключение логгирование
    logging.basicConfig(level=logging.INFO)

    # создаем объект бота
    bot = Bot(token=config.token)

    # Диспечер
    dispecher = Dispatcher()

    dispecher.include_routers(career_choice.router)
    dispecher.include_routers(common.router)
    await dispecher.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
