from src.config.models import Config

token = Config.tg_bot.admin_ids

print(token.__annotations__)