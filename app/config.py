#!/usr/bin/env python
# coding: utf-8

# Импортируем библиотеку для создания объекта настроек проекта
# Требуется предварительно установить pydantic с чтением из файла - "pip install pydantic", "pip install python-dotenv"
from pydantic import BaseSettings

# Импортируем из библиотеки типов данных тип аннотации
from typing import Optional


# Описание настроек проекта
class Settings(BaseSettings):
    PROJECT_NAME: str = 'MovementAcademyLecture'  # название проекта

    VK_BOT_TOKEN: Optional[str]  # токен VK сообщества, берущийся из скрытого файла .env

    DB_PATH: Optional[str]  # путь к БД

    TEXT_WELCOME: Optional[str]  # текст приветственного сообщения
    ATTACHMENT_WELCOME: Optional[str]  # полный id вложения приветственного сообщения

    class Config:  # класс данных для получения значения переменных из файла
        env_file = '.env'  # путь к файлу
        env_file_encoding = 'utf-8'  # кодировка для чтения файла


settings = Settings()  # создание объекта настроек, который содержит все объявленные переменные


# Данные по умолчанию, которые записаны в настройках:
# PROJECT_NAME='MovementAcademyLecture' VK_BOT_TOKEN=None DB_PATH=None TEXT_WELCOME=None ATTACHMENT_WELCOME=None
