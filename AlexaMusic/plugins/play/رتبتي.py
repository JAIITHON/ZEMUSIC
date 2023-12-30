from pyrogram.enums import ChatMemberStatus
from pyrogram import Client, filters
from pyrogram.types import Message
from AlexaMusic import app

#˛ َِ𝗔َِ𝗹َِ𝘀َِ𝗵 .¹#
@app.on_message(filters.command("رتبتي", ""))
async def rotba(_: Client, message: Message):
    user_id = message.from_user.id 
    member = await app.get_chat_member(message.chat.id ,user_id)
    if member.status == ChatMemberStatus.MEMBER: return await message.reply("- رتبتك هي العضو.", reply_to_message_id=message.id)
    elif member.status == ChatMemberStatus.ADMINISTRATOR: return await message.reply("- رتبتك هي الادمن.", reply_to_message_id=message.id)
    elif member.status == ChatMemberStatus.OWNER: return await message.reply("- رتبتك هي المالك.", reply_to_message_id=message.id)
