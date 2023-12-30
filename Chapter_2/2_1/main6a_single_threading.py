import time
import threading
import os

def io_func():
    """Функция имитирует выполнение I/O операции"""
    # Выводим идентификатор потока и PID процесса в котором этот поток существует.
    print(f'Это поток {threading.get_ident()} из процесса {os.getpid()}')
    # Имитация долгой I/O операции.
    time.sleep(1)
#--------------1 вариант последовательная обработка---------------------------------
start = time.time()
io_func()
io_func()
io_func()
print(f'Всего затрачено времени: {time.time() - start}')

