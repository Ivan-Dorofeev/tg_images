import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv
from telegram import InputMediaDocument


def main():
    parser = argparse.ArgumentParser(
        description='Отправляет картинки из папки /image в телеграмм канал '
    )
    parser.add_argument(
        'hours',
        help='Частота повтора отправки (в часах)',
        type=int
    )
    args = parser.parse_args()

    tg_token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['SKY_iIMAGES_CHANNEL_CHAT_ID']

    bot = telegram.Bot(token=tg_token)

    files_list = []
    while True:
        if not files_list:
            for dirpath, dirnames, filenames in os.walk(os.path.join(os.getcwd(), 'images')):
                files_list = filenames
        for file in files_list:
            bot.send_media_group(chat_id=chat_id,
                                 media=[InputMediaDocument(media=open(f'images/{file}', 'rb'))])
        time.sleep(60 * 60 * args.hours)
        random.shuffle(files_list)


if __name__ == '__main__':
    load_dotenv()
    main()
