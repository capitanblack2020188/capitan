import telebot

BOT_TOKEN = "8268214362:AAHr6QVoL77-3Im9Qkg6iN45ZWA1i24VyLU"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! من فعالم 😄")

print("✅ Bot is running...")
bot.polling()
