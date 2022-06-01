# Бот информатор проверки учебных работ DEVMAN
[![Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://telegram.org/)
## Описание
Данная программа делает запрос на сервер [Devman](https://dvmn.org), и с помощью [Telegram](https://telegram.org/) возвращает статус проверки учебных упражнений.

## Как установить
 - Склонировать проект
```shell
git clone https://github.com/toshiharu13/notification_bot.git
```
 - Установить requirements.txt
```shell
pip install -r requirements.txt
```
 - Создать файл .env и заполнить в нем переменные:
 
```dotenv
TG_BOT_TOKEN = 'токен бота от имени которого будут идти оповещения'
```
```dotenv
DVMN_TOKEN = 'токен доступа для API серверов Devman'
```
```dotenv
TG_CHAT_ID = 'ID чата, в который будут идти сообщения бота'
```
## Запуск бота в Docker контейнере локально
 - [Установить Docker](https://docs.docker.com/get-docker/)
 - Cоздать Docker образ c помощью Dockerfile:
```bash
docker build -t <имя_образа> .
```
 - Создать и запустить контейнер на основе получившегося Docker образа:
```bash
docker run --name <имя_контейнера> --env-file .env <имя_образа>
```
Все команды запускаются из корня проекта, файл .env должен быть заполнен
## Цель проекта
Код написан в рамках самостоятельного проекта на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org).