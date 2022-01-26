import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5110027843:AAGPr7xg1BfnvuO4DBpnx7VNV8tueeg3lqE")

    APP_ID = int(os.environ.get("API_ID", "17875613"

    API_HASH = os.environ.get("API_HASH", "6798f54a7f74e94f2ef0923fba8a8377")
