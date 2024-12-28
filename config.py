import os

# MAIN VARS
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
BOT_ADMIN = int(os.getenv("BOT_ADMIN", "")) #Admin Userid

UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "DypixxTech")
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", ""))

# FLOOD WAIT SETTINGS 
ENABLE_FLOOD_WAIT = bool(os.getenv("ENABLE_FLOOD_WAIT", True)) # Set "True" For Enable Floodwait
FLOOD_WAIT_TIME = int(os.getenv("FLOOD_WAIT_TIME", 120))  # Default set 60 seconds

# ALL TEXT'S
FORCE_SUBSCRIBE_TEXT = """<b>{}, 𝖳𝗈 𝗎𝗌𝖾 𝗍𝗁𝖾 𝖻𝗈𝗍 𝗒𝗈𝗎 𝗆𝗎𝗌𝗍 𝗃𝗈𝗂𝗇 𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝖿𝗂𝗋𝗌𝗍. 𝖳𝗁𝖾 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝗇𝗈𝗍 𝗉𝗋𝗈𝖼𝖾𝗌𝗌 𝖺𝗇𝗒 𝗋𝖾𝗊𝗎𝖾𝗌𝗍𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝗃𝗈𝗂𝗇𝗂𝗇𝗀..

बॉट का उपयोग करने के लिए आपको पहले हमारे चैनल में Join होना होगा। बॉट बिना शामिल हुए किसी भी Request को Process नहीं करेगा। ..</b>"""

START_TXT = """𝖧𝖾𝗒, {}!

𝖨 𝖺𝗆 𝖺𝗇 𝖺𝖽𝗏𝖺𝗇𝖼𝖾𝖽 𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆 𝖯𝗁𝗈𝗍𝗈𝗌 𝖺𝗇𝖽 𝗋𝖾𝖾𝗅𝗌 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖻𝗈𝗍 𝗈𝗇 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆. 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖺𝗇𝗒 𝗋𝖾𝖾𝗅 𝗏𝗂𝖽𝖾𝗈𝗌 𝖺𝗇𝖽 𝖯𝗁𝗈𝗍𝗈𝗌 𝖿𝗋𝗈𝗆 𝗆𝖾. 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝗍𝗁𝖾 𝗅𝗂𝗇𝗄 𝗈𝖿 𝗍𝗁𝖾 𝖯𝗁𝗈𝗍𝗈𝗌 𝖺𝗇𝖽 𝗋𝖾𝖾𝗅𝗌.

<blockquote>𝖬𝖺𝖽𝖾 𝖡𝗒 @Dypixx</blockquote>"""

ABOUT_TXT = """📜 𝖢𝗁𝖾𝖼𝗄 𝖠𝖻𝗈𝗎𝗍:

𝖫𝗂𝖻𝗋𝖺𝗋𝗒: 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗺 📚  
𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾: 𝖯𝗒𝗍𝗁𝗈𝗻 🐍
𝖲𝖾𝗋𝗏𝖾𝗋: 𝖲𝖾𝖾𝗇𝗈𝖽𝖾 🌐  
𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌: 𝖵1.0 🚀  
𝖲𝗈𝗎𝗋𝖼𝖾 𝖢𝗈𝖽𝖾: 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 (𝖥𝗋𝖾𝖾) 💻  
𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋: @Dypixx 👨‍💻

<blockquote>𝖬𝖺𝖽𝖾 𝖡𝗒 @Dypixx</blockquote>"""

HELP_TXT = """𝖧𝗈𝗐 𝗍𝗈 𝖴𝗌𝖾:

1. **𝖲𝖾𝗇𝖽 𝗍𝗁𝖾 𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆 𝖯𝗁𝗈𝗍𝗈𝗌 𝖺𝗇𝖽 𝗋𝖾𝖾𝗅𝗌 𝖫𝗂𝗇𝗄:**
𝖲𝗁𝖺𝗋𝖾 𝗍𝗁𝖾 𝖴𝖱𝖫 𝗈𝖿 𝗍𝗁𝖾 𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆 𝖯𝗁𝗈𝗍𝗈𝗌 𝖺𝗇𝖽 𝗋𝖾𝖾𝗅𝗌 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽.

2. **𝖶𝖺𝗂𝗍 𝖿𝗈𝗋 𝖯𝗋𝗈𝖼𝖾𝗌𝗌𝗂𝗇𝗀:** 𝖳𝗁𝖾 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝗉𝗋𝗈𝖼𝖾𝗌𝗌 𝗍𝗁𝖾 𝗅𝗂𝗇𝗄 𝖺𝗇𝖽 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝗍𝗁𝖾 𝖯𝗁𝗈𝗍𝗈𝗌 𝗈𝗋 𝗋𝖾𝖾𝗅𝗌.

3. **𝖱𝖾𝖼𝖾𝗂𝗏𝖾 𝗍𝗁𝖾 𝖵𝗂𝖽𝖾𝗈:** 𝖮𝗇𝖼𝖾 𝗍𝗁𝖾 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝗂𝗌 𝖼𝗈𝗆𝗉𝗅𝖾𝗍𝖾, 𝗍𝗁𝖾 𝗏𝗂𝖽𝖾𝗈 𝗐𝗂𝗅𝗅 𝖻𝖾 𝗌𝖾𝗇𝗍 𝖽𝗂𝗋𝖾𝖼𝗍𝗅𝗒 𝗍𝗈 𝗒𝗈𝗎.

<blockquote>𝖥𝗈𝗋 𝖺𝗇𝗒 𝗂𝗌𝗌𝗎𝖾𝗌 @Dypixx</blockquote>"""
