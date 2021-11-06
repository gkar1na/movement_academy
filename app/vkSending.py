#!/usr/bin/env python
# coding: utf-8

# Импортируем функцию получения рандомного id (необходимо для отправки сообщений)
# Требуется предварительно установить vk_api - "pip install vk_api"
from vk_api.utils import get_random_id

# Импортируем библиотеку для создания задержки воизбежание блока сообщество за спам
import time


# Функция для упрощенной отправки определенного сообщения определенному пользователю из любого модуля
def message(vk, chat_id, message_text, attachment):  # vk - сессия подключения к VK API (будет рассмотрена в файле bot.py)
    vk.messages.send(
        user_id=chat_id,  # chat id пользователя, которому отправляем сообщение
        message=message_text,  # текст отправляемого сообщения
        attachment=attachment,  # id вложения, которое прикрепляется к сообщению
        random_id=get_random_id()  # рандомный id (необходимо по требованиям VK API)
    )  # отправка сообщения

    time.sleep(0.2)  # искусственно созданная задержка
