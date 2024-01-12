import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if BOT_TOKEN is None:
    exit('BOT_TOKEN не найден')

API_KEY = os.getenv('API_KEY')
if API_KEY is None:
    exit('BOT_TOKEN не найден')

API_BASE_URL = 'https://predictor.yandex.net/api/v1/predict.json'

DEFAULT_LANG = 'ru'

# DEFAULT_COMMANDS = (
#     ("start", "Запустить бота"),
#     ("help", "Вывести справку")
# )
