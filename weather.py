import requests
import telebot
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Загрузить переменные среды из файла .env
load_dotenv()

# Получить значение переменной среды
BOT_ID = os.getenv("BOT_ID")
YURY_CHAT_ID = os.getenv("YURY_CHAT_ID")
COMMON_CHAT_ID = os.getenv("COMMON_CHAT_ID")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

bot = telebot.TeleBot(BOT_ID)


def weather_monitoring():
    bot.send_message(
        YURY_CHAT_ID,
        "Weather | Nika monitoring")


def get_weather_forecast(api_key, city):

    # Добавляем к текущей дате необходимое количество дней, чтобы получить ближайшую субботу
    next_saturday = datetime.now() + timedelta((5 - datetime.now().weekday()) % 7)
    saturday_date = next_saturday.strftime('%Y-%m-%d')

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&lang=ru&units=metric"
    response = requests.get(url)
    data = response.json()
    weather_forecast = {}
    for item in data['list']:
        # Проверяем, что дата принадлежит субботе и время равно 6:00, 9:00 или 12:00
        if item['dt_txt'].split()[0] == saturday_date and item['dt_txt'].split()[1] in ['06:00:00', '09:00:00',
                                                                                        '12:00:00']:
            time = item['dt_txt'].split()[1]
            temperature = round(item['main']['temp'])
            description = item['weather'][0]['description']
            icon = item['weather'][0]['icon']
            date = item['dt_txt'].split()[0]
            weather_forecast[time] = {'temperature': temperature, 'description': description, 'icon': icon, 'date': date}

    return weather_forecast


if __name__ == "__main__":

    weather_monitoring()

    api_key = WEATHER_API_KEY
    city = 'Chisinau'

    weather_forecast = get_weather_forecast(api_key, city)
    text = ''
    date = ''
    for time, data in weather_forecast.items():
        trimmed_time = time[:-3]
        text += f"{trimmed_time}:  {data['temperature']}°C, {data['description']}\n"
        date = data['date']

    title = f"⛅️ Погода в субботу ({date})\n"
    final_text = title + text

    bot.send_message(COMMON_CHAT_ID, final_text)
