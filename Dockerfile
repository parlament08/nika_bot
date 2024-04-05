# Используем официальный образ Python
FROM python:3
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app
# Копируем файл requirements.txt в контейнер
COPY requirements.txt .
# Устанавливаем необходимые пакеты из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Устанавливаем пакет cron
RUN apt-get update && apt-get install -y cron
# Копируем файл с заданием cron в контейнер
COPY crontab /etc/cron.d/crontab
# Устанавливаем права доступа для файла cron
RUN chmod 0644 /etc/cron.d/crontab
# Применяем файл cron
RUN /usr/bin/crontab /etc/cron.d/crontab
# Копируем файлы в контейнер
COPY birthday.py .
COPY matches.py .
COPY weather.py .
COPY .env .
CMD printenv > /etc/environment
# Команда по умолчанию для запуска cron
CMD ["cron", "-f"]