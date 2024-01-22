import asyncio


# Корутина для создания задач
async def coro():
    # Получение имени выполняемой задачи
    name = asyncio.current_task().get_name()
    # Сообщение о начале работы задачи
    print(f'{name} начала свою работу!')
    # Имитация выполнения I/O операции
    await asyncio.sleep(1)
    # Сообщение о завершении работы задачи
    print(f'{name} завершена!')


# Корутина для подъема исключения
async def ex_coro():
    await asyncio.sleep(.5)
    # Вызываем исключение
    print('ex_coro поднимает исключение Exсeption')
    raise Exception('Что-то пошло не так!(((')


# Базовая корутина
async def main():
    try:
        # Создание группы задач
        async with asyncio.TaskGroup() as group:
            # Создание трех задач
            tasks = [group.create_task(coro(), name=f'Задача_0{i}') for i in range(1, 4)]
            # Создание задачи, имитирующей возникновение исключения
            tasks.append(group.create_task(ex_coro(), name='Задача_ex'))
    except:
        pass

    # Проверка состояния каждой задачи
    for task in tasks:
        print(f'{task.get_name()}: done={task.done()}, cancelled={task.cancelled()}')
    # Печать сообщения об ошибке в последней задаче
    print(f'{task.get_name()}:{tasks[-1].exception()}')
    for el in tasks: print(el)
    print(*tasks, sep='\n')


asyncio.run(main())

#
# output:
# Задача_01 начала свою работу!
# Задача_02 начала свою работу!
# Задача_03 начала свою работу!
# ex_coro поднимает исключение Exсeption
# Задача_01: done=True, cancelled=True
# Задача_02: done=True, cancelled=True
# Задача_03: done=True, cancelled=True
# Задача_ex: done=True, cancelled=False
# Задача_ex:Что-то пошло не так!(((
# <Task cancelled name='Задача_01' coro=<coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\main6_try_except.py:5>>
# <Task cancelled name='Задача_02' coro=<coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\main6_try_except.py:5>>
# <Task cancelled name='Задача_03' coro=<coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\main6_try_except.py:5>>
