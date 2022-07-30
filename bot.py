import os

import telegram
from dotenv import load_dotenv

load_dotenv()

tg_token = os.environ['TG_BOT_TOKEN']

IvanDorofeev20 = 286730091
sky_images_bot = -1001633240720

bot = telegram.Bot(token=tg_token)
# print(bot.get_me())
# print(bot.get_updates())
# for i in bot.get_updates():
#   print(i['my_chat_member'])
mess = bot.send_message(chat_id=sky_images_bot, text="Привет, тут сообщение")
print(mess)
