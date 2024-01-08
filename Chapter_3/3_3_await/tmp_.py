import asyncio


async def cook_pasta():
    print("Начинаем готовить пасту")
    await asyncio.sleep(1)
    print("Паста готова")


async def cook_sauce():
    print("Начинаем готовить соус")
    await asyncio.sleep(2)
    print("Соус готов")


async def main():
    # task1 = await asyncio.create_task(cook_pasta()) # последовательно, ждет выполнения
    # print('test')                                    # последовательно
    # task2 = await asyncio.create_task(cook_sauce())  # последовательно, ждет выполнения
    # # await asyncio.sleep(3)

    task1 = asyncio.create_task(cook_pasta()) # параллельно
    print('test')                                    # раньше всех
    task2 = asyncio.create_task(cook_sauce())  # параллельно
    await asyncio.sleep(3)


asyncio.run(main())