import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "приемы_пищи"])
async def send_welcome(message: Message):
    await message.answer("Готова принимать твои приёмы пищи 🍽")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)