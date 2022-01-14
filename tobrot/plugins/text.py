import logging
 
import pyrogram
from tobrot import *

from pyrogram import Client, Filters
from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from pyrogram.errors import UserNotParticipant, UserBannedInChannel





################# Start Command ##############
@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(c, m):
    await m.reply_text(
        text=HOME_TEXT.format(m.from_user.first_name),
        disable_web_page_preview=True,
        parse_mode="markdown",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('💡 Help', callback_data='help'),
                    InlineKeyboardButton('📝 About', callback_data='about')
                ],
                [
                    InlineKeyboardButton('Close', callback_data='close')
                ]
            ]
        )
    )



############################# HOME TEXT #####################
 
HOME_TEXT = """Hi.. 🙋
 
💡 **I am a Telegram Leech Bot**
 
🏷️ __I can Leech through torrent, Direct, Ytdl Link and upload to telegram 😌__.
 
 **For check my Features and all commands:**
👉 /help
 
👲 **Maintained By**: [👷 MAXX](https://t.me/MaxxRiderz)"""
