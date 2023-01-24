import os
import configparser

from config.models import Config
from config.models import TgBot

def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path, encoding="utf-8")

    tg_bot = config["tg_bot"]
    webhook = config["webhook"] if not tg_bot.getboolean("use_polling") else None

    return Config(
        tg_bot=TgBot(
            token=tg_bot.get("token", vars=os.environ),
            admin_id=tg_bot.getint("admin_id"),
            num_threads=tg_bot.getint("num_threads"),
            log_file_path=tg_bot.get("log_file_path"),
        )
    )