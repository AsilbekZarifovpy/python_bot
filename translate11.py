from transliterate import to_cyrillic, to_latin
import telebot


TOKEN = '7846970085:AAFQ56206aDQK7mCcTbGw1NcP5gzcZo3TFA'
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu Alykum,"
    javob += "\n Matni kiriting"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)
    
bot.infinity_polling()


# matn = input("Matni kiriting: ")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))