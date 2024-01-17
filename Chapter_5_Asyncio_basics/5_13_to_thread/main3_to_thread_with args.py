import asyncio
import threading
import time


# Блокирующая функция
def blocking_fn(arg1, arg2):
    print(f"Старт blocking_fn() в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")
    time.sleep(arg1)
    print(f"Завершение blocking_fn() в {time.strftime('%X')}")
    return f'В blocking_fn() были переданы два аргмента arg1: {arg1} и arg2: {arg2}'


# Функция асинхронного sleep()
async def sleep_fn():
    print(f"Старт sleep_fn() в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"Завершение sleep_fn() в {time.strftime('%X')}")


async def main():
    print(f"Старт main в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")
    coro = asyncio.to_thread(blocking_fn, 1, 'Привет')
    print(f'Тип объекта coro: {type(coro)}')

    result = await asyncio.gather(coro, sleep_fn(), sleep_fn())
    print(result[0])
    print(f"Завершение main в {time.strftime('%X')}")


start = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {(time.time() - start)}')