import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("���������� ��������� �� ���������, ��� ��� ����������� ���� .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")