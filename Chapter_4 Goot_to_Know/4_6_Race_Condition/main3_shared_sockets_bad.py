# Это псевдокод, демонстрирующий проблему использованиями несколькими корутинами,
# запустить его не получится, т.к. он стучится на несуществующий сервер.

import asyncio
import socket

shared_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет. socket.socket используется для создания объекта сокета

async def read_socket():
    global shared_socket                        # обращаемся к глобальной переменной shared_socket
    data = shared_socket.recv(1024)             # читаем данные из сокета. socket.recv используется для чтения данных из сокета
    print(f"Received data: {data.decode()}")    # печатаем полученные данные

async def write_socket(message):
    global shared_socket                    # обращаемся к глобальной переменной shared_socket
    shared_socket.send(message.encode())    # отправляем данные в сокет. socket.send используется для отправки данных в сокет
    print(f"Sent message: {message}")       # печатаем отправленное сообщение

async def establish_connection():
    global shared_socket                        # обращаемся к глобальной переменной shared_socket
    shared_socket.connect(('localhost', 8888))  # устанавливаем соединение с сервером. socket.connect используется для подключения к серверу

    task1 = asyncio.create_task(read_socket())                   # создаем задачу на чтение данных из сокета. asyncio.create_task используется для создания новой задачи из корутины
    task2 = asyncio.create_task(write_socket("Hello, Server!"))  # создаем задачу на отправку данных в сокет

    await asyncio.gather(task1, task2)  # выполняем все задачи параллельно. asyncio.gather используется для параллельного выполнения задач
    shared_socket.close()               # закрываем сокет. socket.close используется для завершения работы с сокетом

asyncio.run(establish_connection())

