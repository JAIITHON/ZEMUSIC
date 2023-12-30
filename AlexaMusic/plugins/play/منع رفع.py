import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from typing import Union
from AlexaMusic import app
import re
import sys

@app.on_message(command("رفع رقاصه"))
async def yasooo(client, message):
    try:
        
        excluded_user_id = 6186856384
        if message.reply_to_message.from_user.id == excluded_user_id:
            await message.reply_text("ما تكدر ترفع المبرمج ركاصه يالحيوان .")
        else:
            if message.reply_to_message.from_user.mention not in raqsa:
                raqsa.append(message.reply_to_message.from_user.mention)
            await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n رقاصه واحد يذب فلوس عليها 😂💃")
    except Exception as e:
        await message.reply_text(f"حدث خطأ: {e}")


