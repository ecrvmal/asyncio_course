import asyncio
import threading
import time


# Блокирующая функция
def blocking_fn():
    # Печать сообщения о старте и номере используемого потока.
    print(f"Старт blocking_fn() в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")
    # Обратите внимание, что time.sleep() может быть заменен любой блокирующей
    # IO-bound операцией, например операцией с файлами.
    time.sleep(1)  # Имитация выполнения длительной операции.
    print(f"Завершение blocking_fn() в {time.strftime('%X')}")



# Функция асинхронного sleep()
async def sleep_fn():
    # Печать сообщения о старте и номере используемого потока.
    print(f"Старт sleep_fn() в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"Завершение sleep_fn() в {time.strftime('%X')}")


async def main():
    # Печать сообщения о старте и номере используемого потока
    print(f"Старт main в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")
    # Создание корутины, для запуска в независимом потоке
    coro = asyncio.to_thread(blocking_fn)
    # Проверка типа объекта для coro
    print(f'Тип объекта coro: {type(coro)}')
    # Асинхронный запуск задач.
    await asyncio.gather(coro, sleep_fn(), sleep_fn())
    print(f"Завершение main в {time.strftime('%X')}")


start = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {(time.time() - start)}')

# output:
# Старт main в потоке c id 13792 в 12:18:05
# Тип объекта coro: <class 'coroutine'>
# Старт blocking_fn() в потоке c id 12040 в 12:18:05
# Старт sleep_fn() в потоке c id 13792 в 12:18:05
# Старт sleep_fn() в потоке c id 13792 в 12:18:05
# Завершение blocking_fn() в 12:18:06
# Завершение sleep_fn() в 12:18:06
# Завершение sleep_fn() в 12:18:06
# Завершение main в 12:18:06
# Время выполнения программы: 1.0116322040557861