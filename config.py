from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str    # Токен тг

@dataclass
class Config:
    tg_bot: TgBot

# Функция для четения файла .env и возвращать экземпляр
# класса Config с заполненными полями token и admin_ids
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))