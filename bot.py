import os
from dotenv import load_dotenv
load_dotenv()

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import asyncio
from scheduler import start_scheduler  # твоя функция

TOKEN = os.getenv('BOT_TOKEN')  # только env!
if not TOKEN:
    print("ERROR: BOT_TOKEN not set!")
    exit(1)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📅 Open Calendar", web_app=WebAppInfo(url="https://my-call-calendar.vercel.app/"))]],
        resize_keyboard=True
    )
    await message.answer("📅", reply_markup=kb)

async def main():
    print("Starting bot...")
    start_scheduler()  # запускает APScheduler
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())

