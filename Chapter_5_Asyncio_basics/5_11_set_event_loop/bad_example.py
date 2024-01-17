# bad example : several  event_loops in single thread :

import asyncio


async def my_task(idx):
    print(f"Задача {idx} выполняется")
    print(f'Идентификатор цикла задачи: {id(asyncio.get_running_loop())}')
    await asyncio.sleep(idx)
    print(f"Задача {idx} завершена")


async def main():
    print(f'Исходный идентификатор цикла: {id(asyncio.get_running_loop())}')

    # Создаем новый цикл выполнения задач
    loop = asyncio.new_event_loop()

    # Выводим идентификатор нового цикла выполнения
    print(f'Идентификатор нового цикла: {id(loop)}')

    # Устанавливаем новый цикл выполнения как текущий
    asyncio.set_event_loop(loop)

    # Выводим идентификатор текущего цикла выполнения после установки нового
    print(f'Текущий идентификатор цикла: {id(asyncio.get_running_loop())}')

    # Создаем список задач, каждая из которых представляет функцию my_task с разными индексами
    tasks = [asyncio.ensure_future(my_task(i)) for i in range(5)]
    # tasks = [asyncio.create_task(my_task(i)) for i in range(5)]
    # tasks = [my_task(i) for i in range(5)]

    # Ожидаем завершения выполнения всех задач
    await asyncio.gather(*tasks)

    loop.close()


asyncio.run(main())

