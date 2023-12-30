import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AlexaMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait

#˛ َِ𝗔َِ𝗹َِ𝘀َِ𝗵 .¹# </>

@app.on_message(filters.command("تقييد", ""))
def restrict_user(client, message):
    user_id = message.reply_to_message.from_user.id
    
    permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_add_web_page_previews=False,
        can_send_polls=False,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False
    )
    
    client.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=user_id,
        permissions=permissions
    )
    
    client.send_message(message.chat.id, f"ابشر قيدتة {user_id} بنجاح ✓.")
    
#####˛ َِ𝗔َِ𝗹َِ𝘀َِ𝗵 .¹# : T.me/BxxBxxL
#تغير الحقوق دليل فشلك
