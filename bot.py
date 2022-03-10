import os
from pyrogram import Client
from sample_config import Config



devourdevils = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
   plugins=dict(root="programs")
)


    async def stop(self, *args):
        await super().stop()
        print("BRO BOT IS STOPPED BECAUSE YOUR HEROKU DINO IS EXHAUSTED TRANSFER YOUR ANY OTHER HEROKU ACCOUNT TO CONTINUE")


app = Bot()



devourdevils.run()
