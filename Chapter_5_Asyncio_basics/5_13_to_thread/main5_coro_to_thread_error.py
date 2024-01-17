import asyncio

async def соrо():
    print("Вы ошиблись! Я работаю!")
    await asyncio.sleep(1)
    print("Моя работа завершилась!")

async def main():
    # Попытка передать корутину для выполнения в отдельном потоке => error
    await asyncio.to_thread(соrо)

asyncio.run(main())

# output:   Error: sending async function to to_threading
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback