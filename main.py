import os
import telebot

# Obtén el token de tu bot desde BotFather
BOT_TOKEN = "6993929932:AAFhCHQxVC8_RWO_QMr0GqI-A5k77Kt2S58"  # Reemplaza con tu token real
bot = telebot.TeleBot(BOT_TOKEN)

# Manejador para el comando /active
@bot.message_handler(commands=['active'])
def activate_bots(message):
    try:
        # Accede a las páginas web
        web_page1 = "https://spadl.onrender.com/"
        web_page2 = "https://spadl2.onrender.com/"

        # Envía un mensaje de activación
        bot.send_message(message.chat.id, f"Se han activado los bots @hspdlbot y @hspdl2bot. ¡Listos para la acción! 🤖🚀")
    except Exception as e:
        bot.send_message(message.chat.id, f"Hubo un error al activar los bots: {str(e)}")

# Manejador para otros comandos o mensajes
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "¡Comando no reconocido! Usa /active para activar los bots.")

# Inicia el bot
if __name__ == "__main__":
    bot.polling()
