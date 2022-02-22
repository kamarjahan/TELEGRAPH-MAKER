import logging
from tglogging import TelegramLogHandler
import setuptools

# TelegramLogHandler is a custom handler which is inherited from an existing handler. ie, StreamHandler.

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        TelegramLogHandler(
            token="5087114297:AAFnEvhz6_jjJWW_SqWbGJdbMUsQZcCjNik", 
            log_chat_id="-1001666849876", 
            update_interval="2", 
            minimum_lines="1", 
            pending_logs="200000"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("live log streaming to telegram.")








with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="tglogging",
    version="0.0.3",
    author="subinps",
    description="A python package to stream your app logs to a telegram chat in realtime.",
    long_description=readme,
    long_description_content_type="text/markdown",
    project_urls={
        "Tracker": "https://github.com/subinps/tglogging/issues",
        "Source": "https://github.com/subinps/tglogging",
    },
    license="MIT",
    url="https://github.com/subinps/tglogging",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'aiohttp',
        'nest_asyncio'
    ]
)
