import os
from pyrogram import client, filters


@client.on_message(filter.regex(hi))
async def hi(bot, msg):
    await msg.reply_text("hi bro")
