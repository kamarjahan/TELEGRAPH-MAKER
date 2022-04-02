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




START_TEXT = f"""<b> 👋Hello {message.from_user.mention} ,
        
</code>Am a telegraph Uploader That Can Upload Photo, Video And Gif     
Simply send me photo, video or gif under 5MB I will upload it to Telegra.ph
want know more about this bot click help button        
Made With Love By</code> </b> <a href="t.me/devourdevils">DEVOURDEVIL </a>"""

HELP_TEXT = f"""`hello`  {message.from_user.mention},
</code>this bot par may be add somany cool and hot fewtures in feuture want know the
present commands of this bot click or press cmd button
and Just Send Me A Video/gif/photo under 5mb.
i'll upload it to telegra.ph and give you the direct link**</code>"""

CMD_TEXT = f"""Hello  {message.from_user.mention}
  my commands are"""

ID_TEXT = f"""THIS IS YOUR ID  </code>-{message.from_user.id}</code> """

DEV_TEXT = f"""this is my developer information
FIRST NAME:</code>DEVOUR</code>
LAST NAME :</code>DEVIL</code>
USERNAME  :@DEVOURDEVILS
GITHUB PRO:</b> <a href="github.com/kamarjahan">GITHUB </a>
WHO ASKED DEV INFO :{message.from_user.mention}"""

TGP_TEXT = f"""</code>SENT ME A PHOTO,VIDEO,GIF,OR ANY ANIMATION I WILL UPLOADNIT TO TELEGRAPH AND GIVE THE PERMENENT LINK</code>"""

ABOUT_TEXT = f"""
MY NAME:</code>TELEGRAPH BOT</code>
CREATOR:@DEVOURDEVILS
LIBRARY:</code>PYROGRAM</code>
LANGUAGE:</code>PYTHON 3</code>
DATABASE:</code>MONGO DB</code>
        :</code>redislabs</code>
BOT SERVER:</code>railway current</code>
BUILD STATUS:</code>V2.0.0 [edit]</code>"""

STATUS_INFO = f"""
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
   (IDLING)"""


