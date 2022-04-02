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
import random
from programs.pics import ALL_PIC
from pyrogram.errors import UserNotParticipant
from programs.force import force_channel



@Client.on_message(filters.command([df]))
async def fg(bot, msg):
  await reply_text=("hi")
  Message.delete()
