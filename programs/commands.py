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





    
@Client.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[

        InlineKeyboardButton('ADD ME TO GROUP', url='t.me/ddtelegraphbot?startgroup=true'),
    ],
    [

        InlineKeyboardButton('🤔Help', callback_data='help'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [

    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""<b> 👋Hello {message.from_user.mention} ,
        
</code>Am a telegraph Uploader That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif under 5MB I will upload it to Telegra.ph
want know more about this bot click help button
        
Made With Love By</code> </b> <a href="t.me/devourdevils">DEVOURDEVIL </a>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )




@Client.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('🏡Home', callback_data='home'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('⚕️Our group⚕️', url='t.me/septemberfilms'),
        InlineKeyboardButton('cmd', callback_data='cmd')
    ],
    [   
        InlineKeyboardButton('bot info', callback_data='botinfo')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""`hello`  {message.from_user.mention},
</code>this bot par may be add somany cool and hot fewtures in feuture want know the
present commands of this bot click or press cmd button
and Just Send Me A Video/gif/photo under 5mb.
i'll upload it to telegra.ph and give you the direct link**</code>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )




@Client.on_message(filters.command(["cmd"]))
async def cmd(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close'),
        InlineKeyboardButton('id', callback_data='id'),
        InlineKeyboardButton('dev', callback_data='dev'),
    ],
    [
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('mention', callback_data='mention'),
        InlineKeyboardButton('telegraph', callback_data='tgraph'),
        InlineKeyboardButton('username', callback_data='username'),
    ],
    [
        InlineKeyboardButton('tap alert', callback_data='alert'),
        InlineKeyboardButton('botinfo', callback_data='botinfo'),
        InlineKeyboardButton('about', callback_data='about'),
        InlineKeyboardButton('name', callback_data='name')    
    ],
    [
        InlineKeyboardButton('status', callback_data='status'),
        InlineKeyboardButton('covid', callback_data='covid')

    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""Hello  {message.from_user.mention}
  my commands are""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      ) 




@Client.on_message(filters.command(["id"]))
async def id(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('🤔Help', callback_data='help'),
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""THIS IS YOUR ID  </code>-{message.from_user.id}</code> """,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )




@Client.on_message(filters.command(["dev"]))
async def dev(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('🤔Help', callback_data='help'),
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""this is my developer information
FIRST NAME:</code>DEVOUR</code>
LAST NAME :</code>DEVIL</code>
USERNAME  :@DEVOURDEVILS
GITHUB PRO:</b> <a href="github.com/kamarjahan">GITHUB </a>
WHO ASKED DEV INFO :{message.from_user.mention}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )



@Client.on_message(filters.command(["telegraph"]))
async def telegraph(client, message):
  buttons = [[
        InlineKeyboardButton('🏡Home', callback_data='home'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('⚕️Our group⚕️', url='t.me/septemberfilms'),
        InlineKeyboardButton('back⏪', callback_data='cmd')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""</code>SENT ME A PHOTO,VIDEO,GIF,OR ANY ANIMATION I WILL UPLOADNIT TO TELEGRAPH AND GIVE THE PERMENENT LINK</code>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )


@Client.on_message(filters.command(["mention"]))
async def mention(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('back⏪', callback_data='cmd'),
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""THIS IS YOUR PERMENENT LINK {message.from_user.mention}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )



@Client.on_message(filters.command(["username"]))
async def username(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('back⏪', callback_data='cmd'),
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""THIS IS YOUR CURRENT USERNAME @{message.from_user.username}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )




@Client.on_message(filters.command(["name"]))
async def name(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('back⏪', callback_data='cmd'),
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""THIS IS YOUR FIRST AND LAST NAME {message.from_user.first_name} {message.from_user.last_name}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )   
  



@Client.on_message(filters.command(["botinfo"]))
async def botinfo(client, message):
  buttons = [[
        InlineKeyboardButton('back⏪', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('about', callback_data='about')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""</code>hello bro/sis this is the bot information</code>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )   



@Client.on_message(filters.command(["about"]))
async def about(client, message):
  buttons = [[
        InlineKeyboardButton('back⏪', callback_data='botinfo'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('devoleper', url='http://telegram.me/devourdevils'),
        InlineKeyboardButton('deploy own', url='https://heroku.com/deploy?template=https://github.com/kamarjahan/TELEGRAPH-MAKER')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""
MY NAME:</code>TELEGRAPH BOT</code>
CREATOR:@DEVOURDEVILS
LIBRARY:</code>PYROGRAM</code>
LANGUAGE:</code>PYTHON 3</code>
DATABASE:</code>MONGO DB</code>
        :</code>redislabs</code>
BOT SERVER:</code>railway current</code>
BUILD STATUS:</code>V2.0.0 [edit]</code>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id,
      )   





@Client.on_message(filters.command(["status"]))
async def status(client, message):
  buttons = [[
        InlineKeyboardButton('home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('back', callback_data='cmd'),
        InlineKeyboardButton('botinfo', callback_data='botinfo')
    ],
    [
        InlineKeyboardButton('REFRESH', callback_data='refresh')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""
TOTAL TIME:</code>500h</code>
TIME SPENT:</code>96H</code>
TIME LEFT.:</code>404H</code>(THEN IDLING)
BOT STATUS:</code>ACTIVE</code> SINCE 96H
TOTAL USER:</code>4529</code>
TOTAL CHAT:</code>567</code>
BANNEDUSER:</code>56</code>
GLOBAL BAN:</code>8</code>
BOT BANNED:</code>12</code>
BOT ADMINS:</code>452</code>
   (IDLING)""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )   



@Client.on_message(filters.command(["corona"]))
async def corona(client, message):
  buttons = [[
        InlineKeyboardButton('home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('back', callback_data='cmd'),
        InlineKeyboardButton('botinfo', callback_data='botinfo')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""you want to know the covid result in any country use this format /covid [contryname]
eg;- /covid india""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )   

