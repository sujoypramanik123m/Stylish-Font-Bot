import os

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN = int(os.getenv("ADMIN", ""))

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", ""))

DB_URI = os.getenv("DB_URI", "")
DB_NAME = os.getenv("DB_NAME", "")

IS_FSUB = bool(os.environ.get("FSUB", False)) # Set "True" For Force Subscribe Enable
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH

EMOJIS = [
    "👍", "👎", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "😢",
    "🎉", "🤩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🤷‍♂️",
    "❤️‍🔥", "🌚", "💯", "🤣", "⚡", "🏆", "💔", "😐", "🤨", "🍾",
    "💋", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🙈", "🤷‍♀️", "🗿",
    "😇", "🤝", "✍️", "🤗", "🫡", "😨", "🧑‍🎄", "🎄", "⛄", "🤪",
    "🆒", "💘", "🙊", "🦄", "😘", "🙉", "💊", "😎", "👾", "🤷"
]