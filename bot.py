# bot.py
import os
from aiogram import Bot, Dispatcher, executor, types
from scheduler import start_scheduler  # из файла выше

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        types.KeyboardButton(
            text="📅 Open Calendar",
            web_app=types.WebAppInfo(url="https://cv-ai-app-179g.vercel.app/")
        )
    )
    await message.answer("Открой мини‑календарь:", reply_markup=kb)

if __name__ == "__main__":
    start_scheduler()
    executor.start_polling(dp, skip_updates=True)
