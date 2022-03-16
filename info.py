import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = "Media_search"
API_ID = "17875613"
API_HASH = "6798f54a7f74e94f2ef0923fba8a8377"
BOT_TOKEN = "5195945385:AAGxrtvKw-ZDJbq_1MLgmxnG2ThyTGvasCQ"

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]


DATABASE_URI = "mongodb+srv://k:k@cluster0.aeenl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = "telegraph"
COLLECTION_NAME = "Telegram_files"
