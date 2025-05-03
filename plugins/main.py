import asyncio, uuid
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from .fonts import Fonts

font_styles = [
    Fonts.typewriter, Fonts.outline, Fonts.serif, Fonts.bold_cool, Fonts.cool,
    Fonts.smallcap, Fonts.script, Fonts.bold_script, Fonts.tiny, Fonts.comic,
    Fonts.sans, Fonts.slant_san, Fonts.slant, Fonts.sim, Fonts.circles,
    Fonts.dark_circle, Fonts.gothic, Fonts.bold_gothic, Fonts.cloud, Fonts.happy,
    Fonts.sad, Fonts.special, Fonts.square, Fonts.dark_square, Fonts.andalucia,
    Fonts.manga, Fonts.stinky, Fonts.bubbles, Fonts.underline, Fonts.ladybug,
    Fonts.rays, Fonts.birds, Fonts.slash, Fonts.stop, Fonts.skyline,
    Fonts.arrows, Fonts.rvnes, Fonts.strike, Fonts.frozen
]

font_text_cache = {}

async def send_fonts_page(c: Client, msg, page: int, text_id: str, user_text: str, edit=False):
    start_index = (page - 1) * 10
    end_index = start_index + 10
    fonts_for_page = font_styles[start_index:end_index]

    font_message = ""
    for index, style in enumerate(fonts_for_page, start_index + 1):
        styled_text = style(user_text)
        font_message += f"{index}. `{styled_text}`\n\n"

    font_message += "Note: Click on any font to copy it."

    buttons = []
    if page > 1:
        buttons.append(InlineKeyboardButton("⬅️ Back", callback_data=f"back_{page}_{text_id}"))
    if end_index < len(font_styles):
        buttons.append(InlineKeyboardButton("Next ➡️", callback_data=f"next_{page}_{text_id}"))
    else:
        buttons.append(InlineKeyboardButton("❌ Close", callback_data="close"))

    markup = InlineKeyboardMarkup([buttons])

    if edit:
        sent_msg = await msg.edit_text(font_message, reply_markup=markup)
    else:
        sent_msg = await msg.reply_text(font_message, reply_markup=markup)

    async def delete_later():
        await asyncio.sleep(120)
        try:
            await sent_msg.delete()
        except:
            pass

    asyncio.create_task(delete_later())

@Client.on_message(filters.private & filters.text & ~filters.command(["start", "users", "broadcast"]))
async def font_converter(c: Client, m: Message):
    text_id = str(uuid.uuid4())[:8]
    font_text_cache[text_id] = m.text

    async def remove_later():
        await asyncio.sleep(120)
        font_text_cache.pop(text_id, None)

    asyncio.create_task(remove_later())

    await send_fonts_page(c, m, page=1, text_id=text_id, user_text=m.text, edit=False)
