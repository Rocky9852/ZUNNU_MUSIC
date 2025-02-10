#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.
#
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from DnsXMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, User
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden, PeerIdInvalid, ChatAdminRequired
from pyrogram.enums import ChatAction, ChatType, MessageEntityType
from pyrogram import Client, filters, enums
from DnsXMusic.misc import SUDOERS

buttons = [
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", 
            url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"
        ),
    ],
]

@app.on_message(filters.command(["promo"]) & SUDOERS)
async def promos(client, message: Message):
    AMBOT = f"""{app.mention},
🤖 ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛs 🤖
⚡️ғᴇᴀᴛᴜʀᴇs ⚡️
➻ ɪ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢ ɪɴ ɢʀᴏᴜᴘ ᴠᴄ.
➻ ɴᴏ ʟᴀɢ.
➻ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.
➻ 24×7 ᴜᴘᴛɪᴍᴇ.
➻ ʟᴀɢ ғʀᴇᴇ.
"""
    await message.reply(
        text=AMBOT,
        reply_markup=InlineKeyboardMarkup(buttons)
  )
