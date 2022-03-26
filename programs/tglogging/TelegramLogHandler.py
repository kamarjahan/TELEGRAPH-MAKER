import logging
from programs.tglogging import tglogger

# TelegramLogHandler is a custom handler which is inherited from an existing handler. ie, StreamHandler.

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        TelegramLogHandler(
            token="12345678:AbCDEFGhiJklmNoPQRTSUVWxyZ", 
            log_chat_id=-10225533666, 
            update_interval=2, 
            minimum_lines=1, 
            pending_logs=200000),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("live log streaming to telegram.")
