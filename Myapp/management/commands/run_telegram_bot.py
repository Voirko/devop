from datetime import datetime
from django.core.management.base import BaseCommand
import telebot
from Myapp.models import New


bot = telebot.TeleBot("6603637697:AAHZOs4QVwxXCopP3-m2YE4UJfxcSdZfV4s")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['news'])
def news(message):
    news = New.objects.all()
    for new in news:
        bot.send_message(message.chat.id, new.name)


@bot.message_handler(commands=['add'])
def add_product(message):
    if len(message.text.split()) == 3:
        words = message.text.split()
        news_name = words[1]
        news_data = words[2]
        news_data_str = words[2]
        news_data = datetime.strptime(news_data_str, '%Y-%m-%d').date()
        new_product = New(name=news_name, date=news_data)
        new_product.save()

        bot.send_message(message.chat.id, f"News '{news_name}' added successfully!")
    else:
        bot.send_message(message.chat.id, "Invalid format. Use: /add <news_name> <news_data>")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting Bot...")
        bot.polling()
        print("Bot stopped")

