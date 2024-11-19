import asyncio
from tronpy import Tron
from telebot.async_telebot import AsyncTeleBot

bot_token = "Telegram_Bot_Token"

bot = AsyncTeleBot(token=bot_token)


# /start command
@bot.message_handler(commands=['start'])
async def start(message):
    try:
        # response from /start command
        await bot.reply_to(message, "Welcome, use the /generate command to generate a tron wallet")

    except Exception as G:
        print("start:", G)


@bot.message_handler(commands=['generate'])
async def generate(message):
    try:
        # create a Tron user 
        user = Tron()
        # generate a new tron wallet
        account = user.generate_address()
        x = account["base58check_address"]
        y = account["private_key"]
        # send the response to user 
        wallet_info = f"🪙 YOUR NEW TRON WALLET:\n\n" \
               f"🔑 {'ADDRESS'.upper()}: '{x}'\n\n" \
               f"🔒 {'PRIVATE_KEY'.upper()}: '{y}'\n\n" \
               f"⚠️ {'KEEP YOUR PRIVATE KEY SAFE!'.upper()}"
        
        await bot.reply_to(message, wallet_info)
    except Exception as B:
        print("generate_wallet:", B)

asyncio.run(bot.polling())
    

