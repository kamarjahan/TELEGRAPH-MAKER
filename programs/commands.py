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
from programs.donttouch.trl import START_TEXT, HELP_TEXT, CMD_TEXT, ID_TEXT, TGP_TEXT, ABOUT_TEXT, STATUS_INFO, USERNAME 






    
@Client.on_message(filters.command(["start"]))
async def home(client, message):
    if force_channel:
        try:
            user = await client.get_chat_member(force_channel, message.from_user.id)
            if user.status == "you removed":
                await message.reply_text("you are banned")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="PLEASE JOIN OUR UPDATE CHANNEL/GROUP TO USE THIS COMMAND",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("JOIN UPDATE GRP", url=f"t.me/{force_channel}"),
                 ],[
                 InlineKeyboardButton("TRY AGAIN", url=f"http://t.me/{USERNAME}?start=start_")
                 ]]
                )
            )
            return
    reply_markup = InlineKeyboardMarkup( [[
     InlineKeyboardButton('ADD ME TO GROUP', url='t.me/{USERNAME}?startgroup=true'),
     ],[
     InlineKeyboardButton('🤔Help', callback_data='help'),
     InlineKeyboardButton('Close🔐', callback_data='close')
     ]]
     )
    await message.reply_photo(
    photo=random.choice(ALL_PIC),
    caption=f"""{START_TEXT} {message.from_user.mention}""",
     reply_markup=reply_markup,
     parse_mode="html",   
     reply_to_message_id=message.id
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
        caption=f"""{HELP_TEXT} {message.from_user.mention}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.id
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
    caption=f"""{CMD_TEXT} {message.from_user.mention}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.id
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
        caption=f"""{ID_TEXT} </code>-{message.from_user.id}</code>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.id
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
        reply_to_message_id=message.id
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
        caption=f"""{TGP_TEXT}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.id
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
        reply_to_message_id=message.id
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
        reply_to_message_id=message.id
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
        reply_to_message_id=message.id
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
        reply_to_message_id=message.id
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
        caption=f"""{ABOUT_TEXT}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.id,
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
        caption=f"""{STATUS_INFO}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.id
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
        reply_to_message_id=message.id
      )   

