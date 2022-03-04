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


@devourdevils.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ download.....join` @septemberfilms")
  userid = str(message.chat.id)
  img_path = (f"./Download....!/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`Uploading.....`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong join` @septemberfilms for reply") 
  else:
    await msg.edit_text(f"`https://telegra.ph{tlink[0]}`")     
    os.remove(img_path) 

@devourdevils.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ join` @septemberfilms")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....join` @septemberfilms")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"`https://telegra.ph{tlink[0]}`")   
      os.remove(gif_path)   
    except:import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery, Message)
import random


