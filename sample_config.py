import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")
    
    TG_BOT_USERNAME = os.environ.get("TG_BOT_USERNAME", "")
    
    START_MESSAGE = os.environ.get("START_MESSAGE", "")
    
    
    USERNAME = os.environ.get("USERNAME", "")
