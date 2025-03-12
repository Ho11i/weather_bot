import telebot
import requests
import json

bot = telebot.TeleBot('API YOUR TG BOT')
API = 'API FOR WEBSITE OPEN WEATHER'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name},\nНапиши назвагие своего города!')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    town = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={town}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f'Now weather: {data["main"]["temp"]}')
    else:
        bot.reply_to(message, "sorry, but weather in this cite unknow")







bot.polling(non_stop=True)
