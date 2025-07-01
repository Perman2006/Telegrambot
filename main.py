import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

# Bot tokenni Render Environment variables ichidan olish
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Bot va Dispatcher yaratish
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# /start buyrug'iga javob
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("👋 Salom, bot ishlayapti!")

# Web server yaratish
app = web.Application()
SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/webhook")

if __name__ == "__main__":
    setup_application(app, dp, bot=bot)
    web.run_app(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
