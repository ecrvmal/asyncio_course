import asyncio

# Объявление асинхронной функции "my_coroutine"
# Принимает аргумент arg, используется для демонстрации работы корутин
async def my_coroutine(arg):
    await asyncio.sleep(1)  # Ожидаем 1 секунду, используется для имитации задержки выполнения
    print(
        f'Корутина my_coututine создана с помощью {arg}')  # Выводит сообщение, что корутина была создана с помощью arg

async def main():
    # ensure_future превращает корутину в Future объект
    # это необходимо для работы с Future в asyncio
    future = asyncio.ensure_future(my_coroutine('ensure_future'))

    # create_task превращает корутину в Task объект (подкласс Future)
    # это рекомендуемый способ создания задач в asyncio, поскольку Task имеет больше функциональности
    task = asyncio.create_task(my_coroutine('create_task'))

    # Выводим тип объектов future и task
    print(f"ensure_future создаёт объект с типом {type(future)}")  # "ensure_future создает объект типа {type(future)}"
    print(f"create_task создаёт объект с типом  {type(task)}")  # "create_task создает объект типа {type(task)}"

    # Ожидаем завершения задач future и task
    await future
    await task


asyncio.run(main())