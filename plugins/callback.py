from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text
from .main import *

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    data = query.data

    if data == "start":
        await query.message.edit_text(
            text.START.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup[[
    InlineKeyboardButton('❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️', url='https://t.me/UncleChipssBot')
],[
    InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/SuperToppers0'),
    InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ɢʀᴏᴜᴘ', url='https://t.me/SuperToppers')
],[
    InlineKeyboardButton('💝 sᴜʙsᴄʀɪʙᴇ ᴍʏ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ', url='https://youtube.com/@SuperToppers')
],[
    InlineKeyboardButton('👨‍💻 ʜᴇʟᴘ', callback_data='help'),
    InlineKeyboardButton('💁 ᴀʙᴏᴜᴛ', callback_data='about')
]]
        )
    elif data == "help":
        await query.message.edit_text(
            text.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup[[
    InlineKeyboardButton('❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️', url='https://t.me/UncleChipssBot')
],[
    InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/SuperToppers0'),
    InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ɢʀᴏᴜᴘ', url='https://t.me/SuperToppers')
],[
    InlineKeyboardButton('💝 sᴜʙsᴄʀɪʙᴇ ᴍʏ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ', url='https://youtube.com/@SuperToppers')
],[
    InlineKeyboardButton('👨‍💻 ʜᴇʟᴘ', callback_data='help'),
    InlineKeyboardButton('💁 ᴀʙᴏᴜᴛ', callback_data='about')
]]
        )
    elif data == "about":
        await query.message.edit_text(
            text.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💥 ʀᴇᴘᴏ", url="https://github.com"),
                 InlineKeyboardButton("👨‍💻 ᴏᴡɴᴇʀ", url="https://telegram.me/UncleChipssBot")],
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
            ])
        )
    elif data == "close":
        await query.message.delete()

    elif query.data.startswith("next_") or query.data.startswith("back_"):
        _, current_page, text_id = query.data.split("_", 2)  # Get the actual text_id
        if text_id not in font_text_cache:
            return await query.message.edit_text("❗️Your session has expired. Please send /font again.")
        user_text = font_text_cache[text_id]  # Retrieve original text
        new_page = int(current_page) + 1 if query.data.startswith("next") else int(current_page) - 1
        try:
            await send_fonts_page(client, query.message, page=new_page, text_id=text_id, user_text=user_text, edit=True)
        except Exception as e:
            print("Edit error:", e)
