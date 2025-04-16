import os
from telethon import TelegramClient
api_id = "27442555"
api_hash = "0c3c0330b8c3ff16e00aa005bb41245a"
bot_token = ""
skeleton_url = ""

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
skeleton_url = os.environ.get('SKELETON_URL')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


