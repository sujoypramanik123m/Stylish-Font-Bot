import os

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "")
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", ""))
ENABLE_FLOOD_WAIT = bool(os.getenv("ENABLE_FLOOD_WAIT", True)) # Set "True" For Enable Floodwait
FLOOD_WAIT_TIME = int(os.getenv("FLOOD_WAIT_TIME", 300))
