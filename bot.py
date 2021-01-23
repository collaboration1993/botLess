# import config
import requests
#
# bot = telebot.TeleBot(config.token)
#
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли
#     bot.send_message(message.chat.id, message.text)
#
# @bot.message_handler(commands= ['test'])
# def send_voice(message):
#     msg = bot.send_voice(message.chat.id, )
#
#
# if __name__ == '__main__':
#      bot.infinity_polling()

data = {"text":"test"}

req = requests.post('http://127.0.0.1:5000/webhook', json = data)
print(req.text)