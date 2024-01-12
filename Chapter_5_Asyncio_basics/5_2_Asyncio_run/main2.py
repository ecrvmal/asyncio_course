import asyncio


async def coroutine_1():
    await asyncio.sleep(1)
    print("Корутина 1 выполнена")


async def coroutine_2():
    await asyncio.sleep(2)
    print("Корутина 2 выполнена")


async def main():
    # Создаем задачи из корутин
    task1 = asyncio.create_task(coroutine_1())
    task2 = asyncio.create_task(coroutine_2())

    # Запускаем задачи и ждем их выполнения
    await task1
    await task2
    print("Все корутины выполнены")


# Точка входа программы
asyncio.run(main())