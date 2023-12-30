import time
import threading
from threading import Thread
import os


def cpu_func():
    """Функция выполняет CPU bound операцию"""
    start = time.time()
    # Выводим номер потока и номер процесса в котором этот поток существует.
    print(f'Вычисление в потоке {threading.get_ident()} из процесса {os.getpid()}')
    # Вычисления.
    res = sum(a ** a for a in range(5000))
    print(f'Вычисление в потоке {threading.get_ident()} завершено за {time.time() - start}')


# --------------2 вариант используем потоки---------------------------------
# Создание объектов Thread очень похоже на создание Process.
start = time.time()
threads = [Thread(target=cpu_func) for _ in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f'Всего затрачено времени: {time.time() - start}')