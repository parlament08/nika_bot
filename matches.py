from datetime import datetime, timedelta, date
import requests
import telebot
from dotenv import load_dotenv
import os

# Загрузить переменные среды из файла .env
load_dotenv()

# Получить значение переменной среды
BOT_ID = os.getenv("BOT_ID")
YURY_CHAT_ID = os.getenv("YURY_CHAT_ID")
COMMON_CHAT_ID = os.getenv("COMMON_CHAT_ID")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
MATCHES_API_KEY = os.getenv("MATCHES_API_KEY")

bot = telebot.TeleBot(BOT_ID)
# 12.04 (12 апреля)
current_date = date.today().strftime("%d/%m")


def matches_monitoring():
    bot.send_message(
        YURY_CHAT_ID,
        "Matches | Nika monitoring")


def send_top_matches():
    # Замените YOUR_API_KEY на ваш собственный ключ API
    final_text = "⚽ Ближайшие матчи топовых команд:\n\n 🏴󠁧󠁢󠁥󠁮󠁧󠁿🏴󠁧󠁢󠁥󠁮󠁧󠁿🏴󠁧󠁢󠁥󠁮󠁧󠁿 APL 🏴󠁧󠁢󠁥󠁮󠁧󠁿🏴󠁧󠁢󠁥󠁮󠁧󠁿🏴󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮󠁧󠁿\n"

    # URL для получения данных о ближайших матчах в АПЛ
    url_eng = f'https://api.football-data.org/v2/competitions/PL/matches?status=SCHEDULED'
    url_esp = f'https://api.football-data.org/v2/competitions/PD/matches?status=SCHEDULED'
    url_it = f'https://api.football-data.org/v2/competitions/SA/matches?status=SCHEDULED'
    url_ger = f'https://api.football-data.org/v2/competitions/BL1/matches?status=SCHEDULED'
    headers = {'X-Auth-Token': MATCHES_API_KEY}

    # Отправляем запрос к API
    response = requests.get(url_eng, headers=headers)
    data = response.json()

    # Получаем информацию о матчах и командах
    matches = data['matches']

    # Находим матч с участием двух топовых команд
    top_teams = ['Manchester City FC', 'Manchester United FC', 'Chelsea FC', 'Liverpool FC', 'Tottenham Hotspur FC',
                 'Arsenal FC', 'West Ham United FC']  # Пример списка топовых команд

    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']

        # Проверяем, что обе команды являются топовыми
        if home_team in top_teams or away_team in top_teams:
            match_date = datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ')
            match_date = match_date + timedelta(hours=3)
            now = datetime.utcnow()

            # Проверяем, что матч еще не начался
            if (match_date > now) and match_date < (now + timedelta(days=7)):
                final_text += f'⏰{match_date.strftime("%d.%m.%Y %H:%M")}\n  {home_team} - {away_team}\n-----\n'

    final_text += '\n🇪🇸🇪🇸🇪🇸 La Liga 🇪🇸🇪🇸🇪🇸\n'

    response = requests.get(url_esp, headers=headers)
    data = response.json()

    matches = data['matches']

    top_teams = ['Real Madrid CF', 'FC Barcelona']  # Пример списка топовых команд

    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']

        if home_team in top_teams or away_team in top_teams:
            match_date = datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ')
            match_date = match_date + timedelta(hours=3)
            now = datetime.utcnow()

            if (match_date > now) and match_date < (now + timedelta(days=7)):
                final_text += f'⏰{match_date.strftime("%d.%m.%Y %H:%M")}\n  {home_team} - {away_team}\n-----\n'

    final_text += '\n🇮🇹🇮🇹🇮🇹 Seria A 🇮🇹🇮🇹🇮🇹\n'

    response = requests.get(url_it, headers=headers)
    data = response.json()

    matches = data['matches']

    top_teams = ['FC Internazionale Milano', 'AC Milan', 'Juventus FC', 'AS Roma', 'SSC Napoli',
                 'SS Lazio']

    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']

        if home_team in top_teams and away_team in top_teams:
            match_date = datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ')
            match_date = match_date + timedelta(hours=3)
            now = datetime.utcnow()

            if (match_date > now) and match_date < (now + timedelta(days=7)):
                final_text += f'⏰{match_date.strftime("%d.%m.%Y %H:%M")}\n  {home_team} - {away_team}\n-----\n'

    final_text += '\n🇩🇪🇩🇪🇩🇪 Bundesliga 🇩🇪🇩🇪🇩🇪\n'

    response = requests.get(url_ger, headers=headers)
    data = response.json()

    matches = data['matches']

    top_teams = ['FC Bayern München', 'Borussia Dortmund']

    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']

        if home_team in top_teams or away_team in top_teams:
            match_date = datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ')
            match_date = match_date + timedelta(hours=3)
            now = datetime.utcnow()

            if (match_date > now) and match_date < (now + timedelta(days=7)):
                final_text += f'⏰{match_date.strftime("%d.%m.%Y %H:%M")}\n  {home_team} - {away_team}\n-----\n'

    bot.send_message(COMMON_CHAT_ID, final_text)


def main():
    matches_monitoring()
    send_top_matches()


if __name__ == '__main__':
    main()
