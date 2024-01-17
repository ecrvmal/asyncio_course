# Пример с использованием многопоточности и запуска цикла событий в каждом потоке.

import asyncio
import threading

# Асинхронная функция для задачи 1
async def task1(task_id, loop):
    print(f"Задача {task_id} начинается, цикл = {loop}")
    print(f'Идентификатор цикла в задаче {task_id}: {id(asyncio.get_running_loop())}')
    await asyncio.sleep(2)
    print(f"Задача {task_id} завершена")

# Асинхронная функция для задачи 2
async def task2(task_id, loop):
    print(f"Задача {task_id} начинается, цикл = {loop}")
    print(f'Идентификатор цикла в задаче {task_id}: {id(asyncio.get_running_loop())}')
    await asyncio.sleep(3)
    print(f"Задача {task_id} завершена")

# Функция для запуска асинхронных задач в отдельных циклах
def start_loop(loop, coroutine):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coroutine)

# Главная асинхронная функция
async def main():
    print(f'Идентификатор оригинального цикла: {id(asyncio.get_running_loop())}')
    loop1 = asyncio.new_event_loop()
    print(f'Идентификатор первого нового цикла: {id(loop1)}')
    loop2 = asyncio.new_event_loop()
    print(f'Идентификатор второго нового цикла: {id(loop2)}')

    coroutine1 = task1(1, loop1)
    coroutine2 = task2(2, loop2)

    thread1 = threading.Thread(target=start_loop, args=(loop1, coroutine1,))
    thread2 = threading.Thread(target=start_loop, args=(loop2, coroutine2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

asyncio.run(main())