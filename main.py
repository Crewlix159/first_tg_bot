import telebot

bot = telebot.TeleBot("8096091257:AAEBeX057wdp3F9BZi24X_V4LgWGihiDiDo")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    msg = """
Привет!
Я твой Бот!
Вам доступны следующие комманды:
    /start
    /hello"""
    bot.reply_to(message, msg)
@bot.message_handler(commands=["hello"])
def send_hello(message):
    msg = "Тебе тоже привет!"
    bot.reply_to(message, msg)
bot.polling()
