import time
import threading
from threading import Thread
import os

def cpu_func(n):
    """Функция выполняняет CPU bound операцию"""
    start = time.time()
    # Выводим номер потока и номер процесса в котором этот поток существует.
    print(f'Вычисление {n} в потоке {threading.get_ident()} из процесса {os.getpid()}')
    # Вычисления.
    res = sum(a**a for a in range(5000))
    # Время вычислений индивидуально для каждой машины, смотрим сколько t уйдет на одну функцию.
    print(f'Вычисление {n} завершено за {time.time() - start}')

#--------------1 вариант последовательная обработка---------------------------------
start = time.time()
cpu_func(1)
cpu_func(2)
cpu_func(3)
print(f'Всего затрачено времени: {time.time() - start}')