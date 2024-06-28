import os
from pyrogram import Client, filters
from sample_config import Config

# Initialize the Pyrogram Client
Devourdevils = Client(
    "Telegra.ph Uploader",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.TG_BOT_TOKEN,
    plugins=dict(root="programs")
)

# Function to send a message to the user who started the bot
async def send_restart_message(user_id):
    try:
        await Devourdevils.send_message(user_id, "Bot has restarted.")
    except Exception as e:
        print(f"Failed to send restart message: {e}")

# Handler to send message when bot restarts
@Devourdevils.on_restart
async def on_restart():
    print("Bot restarted. Sending message to user...")
    # Replace with the user ID of the user who started the bot
    user_id = '1444445604'  # Update with actual user ID
    await send_restart_message(user_id)

# Print a message indicating bot has started
print("Bot started successfully.")

# Run the bot
Devourdevils.run()






























#import os
#from pyrogram import Client
#from sample_config import Config



#Devourdevils = Client(
#   "Telegra.ph Uploader",
#   api_id=Config.APP_ID,
#   api_hash=Config.API_HASH,
#   bot_token=Config.TG_BOT_TOKEN,
#   plugins=dict(root="programs")
#)

#print("your bot started well or wot")

#Devourdevils.run()
