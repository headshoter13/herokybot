import telebot


def main(message):
    result = 'Привет дружище блин'

    return result


token = '585350425:AAHDIaOX9kINiPB_CmpnUHUYEB_5Tkl6dYg'

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if "/start" in message.text:
        bot.send_message(message.chat.id, "Добро пожаловать в Sentence Simplifier, Введите предложение")
    else:
        bot.send_message(message.chat.id, main(message.text))

if __name__ == '__main__':
     bot.polling(none_stop=True)
