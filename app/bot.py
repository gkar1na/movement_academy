#!/usr/bin/env python
# coding: utf-8

# Импортируем библиотеки для запуска создания таблиц в БД
import subprocess
import sys

# Импортируем библиотеки для взаимодействия с VK API
# Требуется предварительно установить vk_api - "pip install vk_api"
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api

# Импортируем библиотеку для ведения логов
import logging


# Из написанного модуля импортируем настройки проекта
from config import settings

# Из написанного модуля импортируем функцию создания сессии и функции взаимодействия с БД
from database import SessionLocal, VkUser

# Импортируем написанный модуль для отправки сообщений в VK
import vkSending


# Функция запуска бота (для дальнейшего импорта)
def start():

    # Подключение логов
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # время - имя, от которого сохранять лог - уровень - сообщение
        level=logging.INFO  # минимальный уровень выдаваемых логов
    )
    logger = logging.getLogger('vkBot')  # создание объекта для загрузки искусственно созданных логов

    assert subprocess.call([sys.executable, 'database.py']) == 0  # проверка успешного завершения создания таблиц в БД
    logger.info('База данных обновлена')  # создание информативного лога об успешном запуске скрипта создания таблиц в БД

    logger.info('Бот запущен')  # создание информативного лога об успешном запуске скрипта бота

    session = SessionLocal()  # получение сессии подключения к БД

    vk_session = vk_api.VkApi(token=settings.VK_BOT_TOKEN)  # подключение к сообществу через VK API
    longpoll = VkLongPoll(vk_session)  # создание объекта для получения действий в сообщениях сообщества
    vk = vk_session.get_api()  # получение сессии подключения к VK

    # Запуск получения действий в сообщениях сообщества
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user:  # обработка события получаения сообщения от пользователя
            existing_user_chat_ids = {vk_user.chat_id for vk_user in session.query(VkUser)}  # получение сета chat id имеющихся в БД пользователей

            # Добавление данных пользователя в БД и отправка ему приветственного сообщения, если пользователя нет в БД
            if event.user_id not in existing_user_chat_ids:
                vk_user = VkUser(
                    chat_id=event.user_id
                )  # создание объекта-записи в таблице БД VkUser

                session.add(vk_user)  # добавление записи в БД
                session.commit()  # сохранение изменений в БД
                logger.info(f'новый пользователь "{event.user_id}"')  # создание информативного лога об успешном добавлении нового пользователя

                vkSending.message(
                    vk=vk,  # сессия, от имени которой отправлять сообщение
                    chat_id=event.user_id,
                    message_text=settings.TEXT_WELCOME,
                    attachment=settings.ATTACHMENT_WELCOME
                )  # отправка приветственного сообщения

            # Обработка полученных сообщений
            elif event.text:  # если в сообщении есть какой-либо текстовый контент
                if 'привет' in event.text.lower():  # если пользователь написал "Привет" в любом регистре
                    vkSending.message(
                        vk=vk,  # сессия, от имени которой отправлять сообщение
                        chat_id=event.user_id,
                        message_text=settings.TEXT_WELCOME,
                        attachment=settings.ATTACHMENT_WELCOME
                    )  # отправка приветственного сообщения

    session.commit()  # сохранение возможных изменений БД
    session.close()  # завершение сессии подключения к БД
