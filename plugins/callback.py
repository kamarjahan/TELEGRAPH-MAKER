import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery, Message)
import logging


@devourdevils.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
     
        await help(Tgraph, update.message)
      elif "close" in cb_data:
        await update.message.delete() 
      elif "home" in cb_data:
        await update.message.delete()
        await home(Tgraph, update.message)
      elif "help" in cb_data:
        await update.message.delete()
        await help(Tgraph, update.message)
        await help(Tgraph, update.message)
      elif "cmd" in cb_data:
        await update.message.delete()
        await cmd(Tgraph, update.message)   
      

devourdevils.run()
