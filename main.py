import os
import telebot

bot = telebot.TeleBot("API KEY HERE")

@Bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I'm Nidusha Amarasinghe Official Bot.visit My Command List Go To :- https://telegra.ph/Nidusha-Official-Bot-Command-List-12-17")

@bot.message_handler(commands=["supportgroup"])
def send_message (message):
bot.reply_to(message, "https://t.me/Nidusha_Bots")

@bot.message_handler(commands=["updatechannel"])
def send_message (message):
bot.reply_to(message, "https://t.me/Nidushabots_Updates")

@bot.message_handler(commands=["bots"])
def send_message (message):
bot.reply_to(message, "Go To @Nidusha_Bots And Find In There!")

@bot.message_handler(commands=["about"])
def send_message (message):
bot.reply_to(message, "👋😁Hello! I'm Nidusha Amarasinghe's First Programed Bot! Thank You For Using Me😘")

@bot.message_handler(commands=["help"])
def send_message (message):
bot.reply_to(message, "😜Do You Want Help Go To😜 @Nidusha_Bots")

@bot.message_handler(commands=["alive"])
def send_message (message):
bot.reply_to(message, "🤟Hii I'm Online Now😘")

@bot.message_handler(commands=["commands"])
def send_message (message):
bot.reply_to(message, "https://telegra.ph/Nidusha-Official-Bot-Command-List-12-17")

bot.polling()