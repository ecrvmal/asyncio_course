import asyncio

async def my_coro(num):
    # await asyncio.sleep(num)
    if num == 3:
        # raise Exception('file fake.png doesn_t exist')
        with open('fake.png') as f:
            data: str = f.read()
            return data
    elif num == 0:
        raise ValueError("wrong number")
    else:
        return num


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(my_coro(1))
            task2 = tg.create_task(my_coro(0))
            task3 = tg.create_task(my_coro(2))
            task4 = tg.create_task(my_coro(0))
            task5 = tg.create_task(my_coro(3))
            task6 = tg.create_task(my_coro(3))
            tasks = [task1, task2, task3, task4, task5, task6]
            print('all tasks ready', *tasks, sep='\n')
        await tg
    except* ValueError as e:
        for el in e.exceptions:
            print(el)
    except* FileExistsError as e:
        for el in e.exceptions:
            print(el)
    except* Exception as e:
        for el in e.exceptions:
            print(el)
    except:
        pass
    print('all tasks ready', *tasks, sep='\n')
    for el in tasks:
        if el._result:
            print(el._result)
        if el._exception:
            print(el._exception)

asyncio.run(main())

# output:
# all tasks ready
# <Task pending name='Task-2' coro=<my_coro() running at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> cb=[TaskGroup._on_task_done()]>
# <Task pending name='Task-3' coro=<my_coro() running at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> cb=[TaskGroup._on_task_done()]>
# <Task pending name='Task-4' coro=<my_coro() running at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> cb=[TaskGroup._on_task_done()]>
# <Task pending name='Task-5' coro=<my_coro() running at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> cb=[TaskGroup._on_task_done()]>
# <Task pending name='Task-6' coro=<my_coro() running at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> cb=[TaskGroup._on_task_done()]>
# <Task pending name='Task-7' coro=<my_coro() running at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> cb=[TaskGroup._on_task_done()]>
# wrong number
# wrong number
# [Errno 2] No such file or directory: 'fake.png'
# [Errno 2] No such file or directory: 'fake.png'
# all tasks ready
# <Task finished name='Task-2' coro=<my_coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> result=1>
# <Task finished name='Task-3' coro=<my_coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> exception=ValueError('wrong number')>
# <Task finished name='Task-4' coro=<my_coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> result=2>
# <Task finished name='Task-5' coro=<my_coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> exception=ValueError('wrong number')>
# <Task finished name='Task-6' coro=<my_coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> exception=FileNotFoundError(2, 'No such file or directory')>
# <Task finished name='Task-7' coro=<my_coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_14 Task_Group\test8.py:3> exception=FileNotFoundError(2, 'No such file or directory')>
# 1
# wrong number
# 2
# wrong number
# [Errno 2] No such file or directory: 'fake.png'
# [Errno 2] No such file or directory: 'fake.png'
#
# Process finished with exit code 0

