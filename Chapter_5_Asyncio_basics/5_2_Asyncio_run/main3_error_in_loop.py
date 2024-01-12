import asyncio


async def task_func(duration):
    name = asyncio.current_task().get_name()
    print(f'Задача {name} запущена, будет выполнена за {duration} секунд.')
    await asyncio.sleep(duration)
    print(f'Задача {name} завершена.')


async def exeptor(duration):
    await asyncio.sleep(duration)
    # Здесь возникает исключение
    print(f'Задача {asyncio.current_task().get_name()} вызвала ошибку через {duration} секунды')
    raise Exception("Произошла ошибка в main()")


async def main():
    task1 = asyncio.create_task(task_func(3), name='first')
    task2 = asyncio.create_task(task_func(1), name='second')
    task3 = asyncio.create_task(exeptor(2), name='exeption')
    # Асинхронно запускаем все задачи и ждем результат их выполнения
    await asyncio.gather(task1, task2, task3)


try:
    asyncio.run(main())
except Exception as e:
    print(f'Было поднято исключение: {e}')