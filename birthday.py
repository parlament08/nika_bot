from datetime import datetime, date
import telebot

my_id = "390636100"
bot_id = "6497050131:AAEiY1s9lFcjKYauyqZUzG2gNI3a0UUHAP0"
chat_id = "-1001404957939"

bot = telebot.TeleBot(bot_id)
# 12.04 (12 апреля)
current_date = date.today().strftime("%d/%m")

members_data = (
    {"name": "Серёжа", "nickname": "@sergiu", "birth_date": "2020-01-05"},
    {"name": "Слава", "nickname": "@Slava_ot_Dimi", "birth_date": "2020-01-06"},
    {"name": "Эд", "nickname": "@Inko", "birth_date": "2020-01-17"},
    {"name": "Женя", "nickname": "@Eugeniu89", "birth_date": "2020-01-23"},
    {"name": "Паша", "nickname": "@Pasha_Alexandrov", "birth_date": "2020-01-28"},
    {"name": "Вова", "nickname": "@torgan_bg", "birth_date": "2020-03-06"},
    {"name": "Олег", "nickname": "@oleg_sliusarenco", "birth_date": "2020-03-13"},
    {"name": "Денис", "nickname": "@Denis_Pirlog", "birth_date": "2020-03-20"},
    {"name": "Саша", "nickname": "@turevici", "birth_date": "2020-03-31"},
    {"name": "Юра", "nickname": "@iuratv", "birth_date": "2020-04-12"},
    {"name": "Костя", "nickname": "@kostya_prodaus", "birth_date": "2020-05-22"},
    {"name": "Дима", "nickname": "@dumitruc89", "birth_date": "2020-06-01"},
    {"name": "Валера", "nickname": "@vcriv", "birth_date": "2020-08-03"},
    {"name": "Слава", "nickname": "@Slavan", "birth_date": "2020-08-15"},
    {"name": "Боря", "nickname": "@BorisBogoev", "birth_date": "2020-08-27"},
    {"name": "Виталик", "nickname": "@Plague_13", "birth_date": "2020-09-03"},
    {"name": "Виталик", "nickname": "@vitaliepvg", "birth_date": "2020-09-06"},
    {"name": "Андрей", "nickname": "@trufaxD", "birth_date": "2020-09-20"},
    {"name": "Женя", "nickname": "@EvgheniiSidorov", "birth_date": "2020-11-08"},
    {"name": "Вадим", "nickname": "@Vadim_Tintari", "birth_date": "2020-11-19"},
    {"name": "Гриша", "nickname": "@grigorii_f", "birth_date": "2020-11-25"},
    {"name": "Боря", "nickname": "@Boris_Stadnik", "birth_date": "2020-12-17"},
    {"name": "Слава", "nickname": "@Slava_Onov", "birth_date": "2020-12-29"},
    {"name": "Егор", "nickname": "@varzego", "birth_date": "2020-01-25"},
    {"name": "Алекс", "nickname": "@Otokowarai", "birth_date": "2020-09-24"},
    {"name": "Витя", "nickname": "@Victor_Bartean", "birth_date": "2020-05-07"}
)


def birthday_monitoring():
    bot.send_message(
        my_id,
        "Birthday | Nika monitoring")


def send_congrat():
    for el in members_data:
        if str(current_date) == datetime.strptime(el["birth_date"],
                                                  '%Y-%m-%d').strftime('%d/%m'):
            bot.send_message(
                chat_id,
                f'{el["nickname"]} {el["name"]}, Поздравляем с Днём Рождения!!!🥳⚽️👍')


def main():
    birthday_monitoring()
    send_congrat()


if __name__ == '__main__':
    main()
