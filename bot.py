import os
from pyrogram import Client  # Import the Client class from pyrogram
from sample_config import Config  # Import the Config from sample_config

# Initialize the Pyrogram Client
Devourdevils = Client(
    "Telegra.ph Uploader",  # Session name
    api_id=Config.APP_ID,  # Telegram API ID
    api_hash=Config.API_HASH,  # Telegram API Hash
    bot_token=Config.TG_BOT_TOKEN,  # Telegram Bot Token
    plugins=dict(root="programs")  # Plugins directory
)

# Print a message indicating that the bot has started
print("Your bot started successfully.")

# Run the bot
Devourdevils.run()
