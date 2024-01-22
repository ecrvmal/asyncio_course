import asyncio


async def background_timer(n: int):
    print(f'Timer {n} started')
    i = 1
    while i <= n:
        print(f'Прошел {i} тик')
        await asyncio.sleep(1)
        i += 1
    print(f'Timer {n} stopped')
    return 1


async def main():
    task = asyncio.create_task(background_timer(5))
    shielded = asyncio.shield(task)
    await asyncio.sleep(2)
    shielded.cancel()
    print('trying to stop shielded task')
    try:
        await task
    except asyncio.CancelledError:
        print("Отмена задачи")
    else:
        print("Задача успешно выполнена")

    print(f'Обьект задачи {task}')
    print(f'Результат задачи {task.result()}')
    print(f'Обьект щита {shielded}')


asyncio.run(main())

# Timer 5 started
# Прошел 1 тик
# Прошел 2 тик
# trying to stop shielded task
# Прошел 3 тик
# Прошел 4 тик
# Прошел 5 тик
# Timer 5 stopped
# Задача успешно выполнена
# Обьект задачи <Task finished name='Task-2' coro=<background_timer() done, defined at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_13_asyncio_shield\main3_cancel_shield.py:4> result=1>
# Результат задачи 1
# Обьект щита <Future cancelled>
