import asyncio 

from aiogram import Bot, Dispatcher 
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
#Токен скрыть 
Bot_Token = ""

bot = Bot(token = Bot_Token)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_starts(message: Message):
    await message.answer(f'Hello , {message.from_user.first_name} я твой первый бот ')

@dp.message(Command("info"))
async def bot_info(message: Message):
    await message.answer('Инфо о Боте\n'
                         'Версия Бота 1.0\n'
                         'Разработчик(Сардар)\n'
                         )



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

print()