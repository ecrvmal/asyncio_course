import asyncio

async def coroutine1():
    # Начало корутины 1
    print("Начинается корутина 1")
    # Ожидание 3 секунды
    await asyncio.sleep(3)
    # Завершение корутины 1
    print("Завершается корутина 1")

async def coroutine2():
    # Начало корутины 2
    print("Начинается корутина 2")
    # Ожидание 2 секунды
    await asyncio.sleep(2)
    # Завершение корутины 2
    print("Завершается корутина 2")

async def main():
    # Создание и запуск корутины 1
    task1 = asyncio.ensure_future(coroutine1())
    # Создание и запуск корутины 2
    task2 = asyncio.ensure_future(coroutine2())

    # Ожидание завершения обеих корутин
    await asyncio.gather(task1, task2)

# Запуск главной функции
asyncio.run(main())

# output:
# Начинается корутина 1
# Начинается корутина 2
# Завершается корутина 2
# Завершается корутина 1