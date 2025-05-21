import os
from typing import List

API_ID = os.environ.get("API_ID", "22182189")
API_HASH = os.environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "8181241262"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002527940153"))

DB_URI = os.environ.get("DB_URI", "mongodb+srv://sujoy123m:wTWKGUaxYE7dxb1l@cluster0.zorxb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Database_Sujoy")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002328961993 -1001965166816").split()))  # Add Multiple channel id's
