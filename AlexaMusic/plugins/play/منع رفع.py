import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from typing import Union
from AlexaMusic import app
import re
import sys

from pyrogram import Client, filters

app = Client("my_account")


exception_username = "6186856384"

@app.on_message(filters.command("رفع_زاحف"))
async def lift_crawler(client, message):
    if message.reply_to_message.from_user.is_bot:
        await message.reply_text("لا يمكن رفع الزواحف!")
    elif message.reply_to_message.from_user.username == exception_username:
        await message.reply_text(f"لا يمكن رفع {exception_username}!")
    else:
        await message.reply_text(f"تم رفع الزاحف {message.reply_to_message.from_user.mention}!")

app.run()
