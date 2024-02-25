import asyncio

counter = 0
lock = asyncio.Lock()

async def worker_1():

    # Объявляем использование глобальной переменной counter
    global counter

    # Захватываем lock, чтобы исключить конкурентный доступ к counter
    # async with lock:

    # В цикле инкрементируем counter и выводим сообщение
    for i in range(10):
        counter += 1
        print(f"Переменная увеличена на 1 из корутины worker_1, counter = {counter}")

        # Останавливаем выполнение на 1 секунду
        await asyncio.sleep(1)


async def worker_2():

    global counter
    # async with lock:
    for i in range(10):
        counter += 1
        print(f"Переменная увеличена на 1 из корутины worker_2, counter = {counter}")
        await asyncio.sleep(1)


async def main():

    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    await task1
    await task2


asyncio.run(main())


# Переменная увеличена на 1 из корутины worker_1, counter = 1
# Переменная увеличена на 1 из корутины worker_2, counter = 2
# Переменная увеличена на 1 из корутины worker_1, counter = 3
# Переменная увеличена на 1 из корутины worker_2, counter = 4
# Переменная увеличена на 1 из корутины worker_1, counter = 5
# ...