import asyncio

# Это наша функция обратного вызова
def callback(future):
    print(f"Обратный вызов: результат асинхронной операции равен {future.result()}")

async def do_some_work(x):
    print(f"Выполнение некоторой работы: {x}")
    await asyncio.sleep(x)
    return x * 2

async def main():
    task = asyncio.ensure_future(do_some_work(2))   # Создаем задачу, используя ensure_future
    task.add_done_callback(callback)                # Добавляем обратный вызов к задаче
    await task                                      # Дожидаемся завершения работы функции

asyncio.run(main())

