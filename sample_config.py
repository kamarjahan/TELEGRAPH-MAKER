import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")
    
    DATABASE_URL = os.environ.get("DB_URL", "")
    
    DATABASE_NAME = os.environ.get("DB_NAME", "")
    
    
