#!/usr/bin/env python
# coding: utf-8

# Импортируем библиотеку для многопоточности
import threading


# Из написанного модуля импортируем функцию запуска нашего бота
from bot import start


if __name__ == '__main__':  # запуск в случае, когда файл запускается напрямую, а не импортируется из другого скрипта
    bot_thread = threading.Thread(target=start)  # создание потока с нужной функцией запуска
    bot_thread.start()  # запуск функции в потоке
