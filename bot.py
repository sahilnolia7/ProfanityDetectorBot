import telebot

token='1932205423:AAHvWpjvREB30qhNhPsv0EDk9hhfkleUPtI'
bot = telebot.TeleBot(token)
GROUP_ID= -1001587099350
blacklist=['hello']
@bot.message_handler(content_types=["text"])
def handle_text(message):
    for x in blacklist:
        if(x in message.text):
            bot.delete_message(message.chat.id, message.message_id)
        else:
            pass
        
if __name__ == "__main__":
    bot.infinity_polling()
