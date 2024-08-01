
import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
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




# Define constants for API credentials (for bot itself)
BOT_API_ID = "17875613"
BOT_API_HASH = "6798f54a7f74e94f2ef0923fba8a8377"
BOT_TOKEN = "5195945385:AAGxrtvKw-ZDJbq_1MLgmxnG2ThyTGvasCQ"

# Create the bot instance
app = Client("my_bot", api_id=BOT_API_ID, api_hash=BOT_API_HASH, bot_token=BOT_TOKEN)

# Store user sessions
user_sessions = {}

@Client.on_message(filters.command(["apinfo"]))
async def apinfo(client, message):
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton('Login', callback_data='login')]]
    )
    await message.reply_text("Welcome! Please login to use the bot.", reply_markup=reply_markup)

@app.on_callback_query(filters.regex("login"))
async def login(client, callback_query):
    await callback_query.message.reply_text("Please send your phone number in the format +1234567890.")
    user_sessions[callback_query.from_user.id] = {"state": "phone_number"}

@Client.on_message(filters.private & filters.text)
async def handle_message(client, message):
    user_id = message.from_user.id

    if user_id in user_sessions:
        session = user_sessions[user_id]

        if session["state"] == "phone_number":
            phone_number = message.text
            session["phone_number"] = phone_number
            await message.reply_text(f"Sending OTP to {phone_number}...")
            try:
                session["client"] = Client("user_session", api_id=BOT_API_ID, api_hash=BOT_API_HASH)
                await session["client"].connect()
                await session["client"].send_code(phone_number)
                session["state"] = "otp"
                await message.reply_text("Please enter the OTP you received.")
            except Exception as e:
                await message.reply_text(f"Failed to send OTP: {e}")

        elif session["state"] == "otp":
            otp = message.text
            phone_number = session["phone_number"]
            try:
                await session["client"].sign_in(phone_number, otp)
                user_info = await session["client"].get_me()
                api_id, api_hash = user_info.id, user_info.access_hash
                await message.reply_text(f"Login successful! Your API ID: {api_id}, API Hash: {api_hash}")
                session["state"] = "logged_in"
            except Exception as e:
                await message.reply_text(f"Failed to login: {e}")
