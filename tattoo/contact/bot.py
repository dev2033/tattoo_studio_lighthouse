import telebot
from telebot.types import Message

from .models import AdminTelegramId


token = '1418476569:AAFM3y0nJWyfBVw_B2ySrnQ9I7nXal4g9o8'
bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda message: True)
def send_msg(message: Message):
    masters_id = AdminTelegramId.objects.all()
    for _id in masters_id.telegram_id:
        bot.send_message(_id, message.text)

#
# if __name__ == '__main__':
#     print('start bot ')
#     bot.polling()
