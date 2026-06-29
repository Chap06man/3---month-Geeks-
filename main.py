import asyncio 

from aiogram import Bot, Dispatcher 
from aiogram.types import Message
from aiogram.filters import CommandStart, Command 
#o
Bot_Token = "8940390700:AAH0mYwT4VUD05sTFR0m2R3_o628RPuQbH"

bot = Bot(token = Bot_Token)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_starts(message: Message):
    await message.answer(f'Hello , {message.from_user.first_name} я твой первый бот ')



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

print()