import os

API_ID    = os.environ.get("API_ID", "19957434")
API_HASH  = os.environ.get("API_HASH", "a27e2ed25f103d68455e54009e0b5367")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
