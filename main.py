import telebot

BOT_TOKEN = "8268214362:AAHr6QVoL77-3Im9Qkg6iN45ZWA1i24VyLU"  # ← اینجا توکن واقعی رباتت رو بگذار

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! من فعالم 😁")

# این خط باعث میشه ربات همیشه روشن بمونه
bot.infinity_polling()
