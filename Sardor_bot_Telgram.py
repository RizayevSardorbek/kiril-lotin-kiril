from transliterate import to_latin, to_cyrillic
import telebot

TOKEN = "2135307094:AAGVHeMAQxfqhByso1u90n1lXIlkKIwfuhI"

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu-allaykum, lotin_kiril_lotin botiga xush kelibsiz!!!"
    javob += "\nMarhamat matn kiritishingiz mumkin!"
    bot.reply_to(message, javob)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.infinity_polling()
