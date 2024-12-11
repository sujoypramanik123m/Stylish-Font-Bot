from config import *
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import instaloader
import os
import shutil
import time
user_last_download_time = {}

# Developer: @Dypixx, Dont Remove Credits.
app = Client("insta_reels_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(START_TXT.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Help", callback_data="help"),
             InlineKeyboardButton("About", callback_data="about")]
        ]))

# ============== #
# MAIN FUNCTION 
# ============== #

@app.on_message(filters.text)
async def download_instagram_content(client, message):
    if message.text.startswith("/"):
        return
    try:
        if UPDATE_CHANNEL:
            try:
                user = await client.get_chat_member(UPDATE_CHANNEL, message.chat.id)
                if user.status == "kicked":
                    await message.reply_text("𝖸𝗈𝗎 𝖺𝗋𝖾 𝖻𝖺𝗇𝗇𝖾𝖽 🚫")
                    return
            except UserNotParticipant:
                await message.reply_text(
                    text=FORCE_SUBSCRIBE_TEXT.format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Join Now", url=f"https://telegram.me/{UPDATE_CHANNEL}")]]
                    )
                )
                return
            except Exception as error:
                print(error)
                await message.reply_text(f"{str(error)}")
                return

        if ENABLE_FLOOD_WAIT:
            current_time = time.time()
            last_download_time = user_last_download_time.get(message.chat.id, 0)
            remaining_time = FLOOD_WAIT_TIME - (current_time - last_download_time)
            if remaining_time > 0:
                minutes, seconds = divmod(int(remaining_time), 60)
                time_text = f"{minutes} 𝗆𝗂𝗇𝗎𝗍𝖾 & {seconds} 𝗌𝖾𝖼𝗈𝗇𝖽𝗌" if minutes > 0 else f"{seconds} 𝗌𝖾𝖼𝗈𝗇𝖽𝗌"
                await message.reply_text(f"𝖸𝗈𝗎 𝖼𝖺𝗇 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖺𝗇𝗈𝗍𝗁𝖾𝗋 𝖼𝗈𝗇𝗍𝖾𝗇𝗍 𝖺𝖿𝗍𝖾𝗋 {time_text}!")
                return
            else:
                user_last_download_time[message.chat.id] = current_time

        url = message.text.strip()
        if not url.startswith("https://www.instagram.com/"):
            await message.reply("𝖯𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗇𝖽 𝖺 𝗏𝖺𝗅𝗂𝖽 𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆 𝖴𝖱𝖫 (𝖱𝖾𝖾𝗅 𝗈𝗋 𝖯𝗁𝗈𝗍𝗈𝗌)")
            return

        L = instaloader.Instaloader()
        download_dir = "downloads"
        os.makedirs(download_dir, exist_ok=True)

        if "/reel/" in url or "/p/" in url:
            shortcode = url.split("/")[-2]
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            L.download_post(post, target=download_dir)
        else:
            await message.reply("𝖳𝗁𝗂𝗌 𝖴𝖱𝖫 𝗍𝗒𝗉𝖾 𝗂𝗌 𝗇𝗈𝗍 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝖾𝖽.")
            return

        T = await message.reply("𝖳𝗋𝗒𝗂𝗇𝗀 𝗍𝗈 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽...")
        downloaded_files = os.listdir(download_dir)
        total_photos = 0
        for file in downloaded_files:
            file_path = os.path.join(download_dir, file)
            if file_path.endswith((".mp4", ".jpg", ".png")):
                if file_path.endswith(".mp4"):
                    await message.reply_video(video=file_path)
                else:
                    await message.reply_document(document=file_path)
                    total_photos += 1
                os.remove(file_path)

        shutil.rmtree(download_dir)
        await T.delete()
        if total_photos > 0:
            await message.reply(f"𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽𝖾𝖽 {total_photos} 𝗉𝗁𝗈𝗍𝗈𝗌 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒!")
    except IndexError:
        await message.reply("𝖯𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗇𝖽 𝖺 𝗏𝖺𝗅𝗂𝖽 𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆 𝖴𝖱𝖫")
    except Exception as e:
        await message.reply(f"𝖤𝗋𝗋𝗈𝗋 𝗈𝖼𝖼𝗎𝗋𝗋𝖾𝖽: {str(e)}")


# ============== #
# CALLBACKS DATA
# ============== #

@app.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "help":
        await query.message.edit_text(HELP_TXT, reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('About', callback_data='about'),
              InlineKeyboardButton('Back', callback_data='back')]]))
    elif query.data == "about":
        await query.message.edit_text(ABOUT_TXT, reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('Help', callback_data='help')],
             [InlineKeyboardButton('Back', callback_data='back'),
              InlineKeyboardButton('Source Code', user_id=int(BOT_ADMIN))]]))
    elif query.data == "back":
        await query.message.edit_text(START_TXT.format(query.from_user.mention), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help", callback_data="help"), InlineKeyboardButton("About", callback_data="about")]]))

app.run()
# Developer: @Dypixx, Dont Remove Credits.
