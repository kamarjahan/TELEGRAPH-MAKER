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

devourdevils = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

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
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
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
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
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

devourdevils = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@devourdevils.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ join` @septemberfilms")
  userid = str(message.chat.id)
  img_path = (f"./Download....!/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`Uploading..... join` @septemberfilms")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong join` @septemberfilms") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@devourdevils.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ join` @septemberfilms")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Something really Happend Wrong... join @septemberfilms") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb join @septemberfilms")
    
    
    
    
    
@devourdevils.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ join` @septemberfilms")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Something really Happend Wrong... join @septemberfilms"") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb join @septemberfilms"")

    
    
    
ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]
    
    
    
    
    
@devourdevils.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[

        InlineKeyboardButton('ADD ME TO GROUP', url='t.me/ddtelegraphbot?startgroup=true'),
    ],
    [

        InlineKeyboardButton('🤔Help', callback_data='help'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('🗣️Any Doubt', url='http://telegram.me/devourdevils'),
        InlineKeyboardButton('Source Code📃', url='https://github.com/kamarjahan/TELEGRAPH-MAKER')
    ],
    [
        InlineKeyboardButton('Dev', url='t.me/devourdevils'),
        InlineKeyboardButton('support ChAT', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await devourdevils.send_photo(
        photo=random.choice(ALL_PIC),
        chat_id=message.chat.id,
        caption=f"""<b>👋Hello {message.from_user.mention} ,
        
`Am a telegraph Uploader That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif under 5MB I will upload it to Telegra.ph
want know more about this bot click help button
        
Made With Love By` </b> <a href="t.me/devourdevils">DEVOURDEVIL </a>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )


ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]




@devourdevils.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('🏡Home', callback_data='home'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('⚕️Our group⚕️', url='t.me/septemberfilms'),
        InlineKeyboardButton('cmd', callback_data='cmd')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await devourdevils.send_photo(
        photo=random.choice(ALL_PIC),
        chat_id=message.chat.id,
        caption=f"""hello  {message.from_user.mention},
this bot par may be add somany cool and hot fewtures in feuture want know the
present commands of this bot click or press cmd button
and Just Send Me A Video/gif/photo under 5mb.
i'll upload it to telegra.ph and give you the direct link**""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )


ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]





@devourdevils.on_message(filters.command(["cmd"]))
async def cmd(client, message):
  buttons = [[
        InlineKeyboardButton('🏡Home', callback_data='home'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms'),
        InlineKeyboardButton('🤔Help', callback_data='help')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await devourdevils.send_photo(
        photo=random.choice(ALL_PIC),
        chat_id=message.chat.id,
        caption=f"""Hello  {message.from_user.mention}
  my commands are
  /id to get your id
  /dev to get my developers
  /cr  to my crt""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      ) 




@devourdevils.on_message(filters.command("id")) 
async def id(client, message):
    text = f"""this is your id `-{message.from_user.id}`"""
    
    
    
    await message.reply_text(text=text)
          
        

        
@devourdevils.on_message(filters.command("dev")) 
async def dev(client, message):
    await message.reply_text(
        text=f"""this is my developer information
FIRST NAME:`DEVOUR`
LAST NAME :`DEVIL`
USERNAME  :@DEVOURDEVILS
GITHUB PRO:</b> <a href="github.com/kamarjahan">GITHUB </a>
WHO ASKED DEV INFO :{message.from_user.mention}""", disable_web_page_preview=True,
        
         
    )
   
    
    

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
