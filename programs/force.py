import os
from pyrogram.types import InlineKeyBoardMarkup, InlineKeyboardButton
from pyrograms.errors import UserNotParticipant
from pyrogram import client, filters

force_channel = "septemberfilms"


@client.on_message(filters.command(["force"]))
acync def force(client,msg):
        if force_channel:
        try:
            user = await client.get_chat_member(force_channel, msg.from_user.id)
            if user.status == "you removed":
                await msg.reply_text("you are banned")
                return
        except UserNotParticipant:
             await msg.reply_text(
                 text="your not sub my grp",
                 reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("join update", url=f"t.me/{force_channel}")
                  ]]
                 )
            )
            return
    await msg.reply_text(
        text="hi"
)








