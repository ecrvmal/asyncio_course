import asyncio

async def set_after(fut, delay):
    # Задержка на `delay` секунд.
    await asyncio.sleep(delay)
    try:
        # установка 'Future' в результат
        # доступно только объекту Future.
        fut.set_result('Future')
        print('function "set_after", parameter is future ')
    except asyncio.InvalidStateError:
        # Для Task попадаем сюда т.к. будет выброшено исключение
        print('function "set_after", parameter is task ')
        return "Task"

async def main():
    # Получим текущий цикл событий.
    loop = asyncio.get_event_loop()
    # Создадим новый объект Future.
    fut = loop.create_future()

    asyncio.ensure_future(set_after(fut, .1))
    print(f'Создан объект {type(fut)}')
    # Ждем, пока `fut` не получит результат
    # (0.1 секунды), после печатаем его.
    res = await fut
    print(f'Проверено! Это объект {res}!')
    # Создаем объект Task
    task = asyncio.create_task(set_after(fut, 1))
    print(f'Создан объект {type(task)}')
    res = await task
    print(f'Проверено! Это объект {res}!')

asyncio.run(main())