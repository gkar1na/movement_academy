#!/usr/bin/env python
# coding: utf-8

# ORM - технология программирования, которая связывает базы данных с концепциями
# объектно-ориентированных языков программирования, создавая «виртуальную объектную базу данных»
# Импортируем ORM (Object-Relational Mapping) библиотеку для взаимодействия с БД
# Требуется предварительно установить sqlalchemy - "pip install sqlalchemy", "pip install psycopg2-binary"
from sqlalchemy import Column, Integer  # импорт объекта столбец и типа данных в БД "int"
from sqlalchemy.ext.declarative import declarative_base  # импорт функции создания БД
from sqlalchemy.orm import sessionmaker  # импорт функции создания мейкера сессий
from sqlalchemy import create_engine  # импорт функции создания движка взаимодействия с БД

# Из написанного модуля импортируем настройки проекта
from config import settings


db = declarative_base()  # создание объекта БД
engine = create_engine(settings.DB_PATH)  # создание движка взаимодействия с БД
SessionLocal = sessionmaker(bind=engine)  # создание мейкера сессий


# Описание таблицы пользователей в БД
class VkUser(db):
    __tablename__ = 'vk_user'  # название таблицы

    # PRIMARY KEY — первичный ключ, ограничение, позволяющее однозначно идентифицировать каждую запись в таблице БД
    chat_id = Column(Integer, primary_key=True)  # столбец для хранения chat id пользователей; типа данных в таблице - "int"; столбец является первичным ключом


if __name__ == '__main__':  # запуск в случае, когда файл запускается напрямую, а не импортируется из другого скрипта
    db.metadata.create_all(engine)  # создание в БД всех объявленных в файле объектов (таблица с названием vk_user)
