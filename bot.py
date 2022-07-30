import os
import time

import telegram
from dotenv import load_dotenv
from telegram import InputMediaDocument

load_dotenv()

tg_token = os.environ['TG_BOT_TOKEN']

IvanDorofeev20 = 286730091
sky_images_bot = -1001633240720

if __name__ == '__main__':
    bot = telegram.Bot(token=tg_token)

    while True:
        for dirpath, dirnames, filenames in os.walk(os.path.join(os.getcwd(), 'images')):
            for filename in filenames:
                send_img = bot.send_media_group(chat_id=sky_images_bot, media=[
                    InputMediaDocument(media=open(f'images/{filename}', 'rb'))])
                time.sleep(60 * 60 * 4)
