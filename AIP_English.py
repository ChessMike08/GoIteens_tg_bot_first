import requests
from aiogram import Bot
from aiogram.types import BotCommand

from Key_English import KEY_ENG
import json

def muf(word):
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': KEY_ENG})
    response_str = response.text
    response_json = json.loads(response_str)
    return response_json

def get_sin(word):
    data = muf(word)
    return data.get('synonyms')

def get_ant(word):
    data = muf(word)
    return data.get('antonyms')

async def set_all_default_comand(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('start', 'Start or restart bot'),
            BotCommand('restart', 'Start or restart bot'),
            BotCommand('help', 'Get help'),
            BotCommand('board', 'View the board'),
            BotCommand('gratitude_board', 'View the board')
        ],
    )