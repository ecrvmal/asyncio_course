import asyncio

async def foo():
    print("Запущена корутина foo")
    await asyncio.sleep(5)
    raise Exception("Ошибка в foo")
    print("Явное переключение контекста обратно на foo")

async def bar():
    print("Запущена корутина bar")
    await asyncio.sleep(3)
    raise Exception("Ошибка в bar")
    print("Явное переключение контекста обратно на bar")

async def main():
    tasks = [asyncio.create_task(foo()), asyncio.create_task(bar())]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)

    for task in done:
        print("Задание завершено: ", task)
        if task.exception() is not None:
            print("Исключение задачи: ", task.exception())
    for task in pending:
        print("Задача в ожидании: ", task)
        await task   # приостановлено, выполнится, выдаст ошибку Exception: Ошибка в foo

    # await asyncio.gather(*tasks)

asyncio.run(main())