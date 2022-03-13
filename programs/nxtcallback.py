import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery, Message)
from programs.commands import cmd, help, home, dev, id, mention, telegraph, name, username, botinfo, about, status, corona
#dont remove this this is must







@Client.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "covid" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await corona(Tgraph, update.message)
