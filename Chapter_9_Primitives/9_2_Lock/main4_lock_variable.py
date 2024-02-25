import asyncio

# Объявляем глобальную переменную counter со значением 0
counter = 0

# Создаем объект lock для управления доступом к counter
lock = asyncio.Lock()


# Объявляем асинхронную функцию worker_1
async def worker_1():

    # Объявляем использование глобальной переменной counter
    global counter

    # Захватываем lock, чтобы исключить конкурентный доступ к counter
    async with lock:

        # В цикле инкрементируем counter и выводим сообщение
        for i in range(10):
            counter += 1
            print(f"Переменная увеличена на 1 из корутины worker_1, counter = {counter}")

            # Останавливаем выполнение на 1 секунду
            await asyncio.sleep(1)


# Объявляем асинхронную функцию worker_2, аналогичную worker_1
async def worker_2():

    global counter
    async with lock:
        for i in range(10):
            counter += 1
            print(f"Переменная увеличена на 1 из корутины worker_2, counter = {counter}")
            await asyncio.sleep(1)


# Объявляем асинхронную функцию main
async def main():

    # Создаем задачу task1 из worker_1
    task1 = asyncio.create_task(worker_1())

    # Создаем задачу task2 из worker_2

    task2 = asyncio.create_task(worker_2())
    # Ждем завершения task1
    await task1

    # Ждем завершения task2
    await task2


# Запускаем основную функцию main с помощью asyncio.run
asyncio.run(main())


# Переменная увеличена на 1 из корутины worker_1, counter = 1
# Переменная увеличена на 1 из корутины worker_1, counter = 2
# ...
# Переменная увеличена на 1 из корутины worker_1, counter = 9
# Переменная увеличена на 1 из корутины worker_1, counter = 10
# Переменная увеличена на 1 из корутины worker_2, counter = 11
# Переменная увеличена на 1 из корутины worker_2, counter = 12
# ....
# Переменная увеличена на 1 из корутины worker_2, counter = 19
# Переменная увеличена на 1 из корутины worker_2, counter = 20