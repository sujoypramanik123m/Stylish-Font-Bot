from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text
from .main import send_fonts_page

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    data = query.data

    if data == "start":
        await query.message.edit_text(
            text.START.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
                 InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help")],
                [InlineKeyboardButton("♻ ᴅᴇᴠᴇʟᴏᴘᴇʀ ♻", url="https://telegram.me/TechifyRahul")]
            ])
        )
    elif data == "help":
        await query.message.edit_text(
            text.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ᴜᴩᴅᴀᴛᴇꜱ", url="https://telegram.me/Techifybots"),
                 InlineKeyboardButton("ꜱᴜᴩᴩᴏʀᴛ", url="https://telegram.me/TechifySupport")],
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
            ])
        )
    elif data == "about":
        await query.message.edit_text(
            text.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💥 ʀᴇᴘᴏ", url="https://github.com/TechifyBots/Stylish-Font-Bot"),
                 InlineKeyboardButton("👨‍💻 ᴏᴡɴᴇʀ", url="https://telegram.me/TechifyRahul")],
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
            ])
        )
    elif data == "close":
        await query.message.delete()
    elif data.startswith("next_") or data.startswith("back_"):
        _, current_page, *text_parts = data.split("_")
        user_text = "_".join(text_parts)
        new_page = int(current_page) + 1 if data.startswith("next") else int(current_page) - 1

        try:
            await send_fonts_page(client, query.message, page=new_page, user_text=user_text, edit=True)
        except Exception as e:
            print("Edit error:", e)
