import os
import time

import pyrogram
from pyrogram import Client, enums

APP_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
OWNER_ID = os.environ.get("OWNER_ID", 'mmagneto') # Telegram kullanıcı adı girin.
    
