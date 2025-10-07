
import telebot

BOT_TOKEN = "8268214362:AAGYbs3I-xcWnmRAh62DNz7F2fHGhh10ung"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! من فعالم 😁")

# --- این دو خط رو اضافه کن ---
bot.remove_webhook()
bot.polling(none_stop=True)
