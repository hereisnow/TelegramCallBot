import os
from dotenv import load_dotenv  # добавь
load_dotenv()  # загрузи .env или Railway vars

from aiogram import Bot, Dispatcher, F  # 3.x API
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
from scheduler import startscheduler, schedulereminder  # твои funcs

TOKEN = os.getenv('8597331437:AAHZr-xUlML25RwGBG_U89kHKBzX-W-5rMM')
if not TOKEN:
    raise ValueError("BOT_TOKEN not set!")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
    kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Open Calendar", web_app=WebAppInfo(url="https://my-call-calendar.vercel.app/"))]], resize_keyboard=True)
    await message.answer("📅", reply_markup=kb)

# пример schedulereminder
# schedulereminder(chat_id, run_dt, text)

async def main():
    startscheduler()  # запускай scheduler
    await dp.start_polling(bot, skip_updates=True)  # 3.x polling!

if __name__ == '__main__':
    asyncio.run(main())
