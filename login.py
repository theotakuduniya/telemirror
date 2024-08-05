"""
Prints telegram session string key
"""
try:
    from config import API_HASH, API_ID
except Exception:
    print("Failed load API_HASH and API_ID from .env")
    API_HASH = input("Input telegram API_HASH:6c0ea77e38c2286a9d4d7b1bd0f07bd5 ")
    API_ID = input("Input telegram API_ID:21778536")
from telethon import TelegramClient
from telethon.sessions import StringSession

with TelegramClient(
    session=StringSession(), api_id=API_ID, api_hash=API_HASH
) as client:
    print("Session string: ", client.session.save())
