import asyncio

async def me_coro(name, delay):
    await asyncio.sleep(delay)
    print(f"Задача {name} выполнена")

async def main():
    tasks = [asyncio.create_task(me_coro(f"task_{i}", i+1)) for i in range(5)]
    done, pending = await asyncio.wait(tasks, timeout=2, return_when=asyncio.ALL_COMPLETED)
    print(f'{done=}   {pending=}')
    for task in pending:
        task.cancel()
    result = len(done), len(pending)
    print(result)


asyncio.run(main())

# Задача task_0 выполнена
# Задача task_1 выполнена
# done={<Task finished name='Task-3' coro=<me_coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_5_Asyncio_basics\5_7_asyncio_wait\tmp.py:3> result=None>, <Task finished name='Task-2' coro=<me_coro() done, defined at D:\GB\pythonProject\asyncio\Chapter_5_Asyncio_basics\5_7_asyncio_wait\tmp.py:3> result=None>}   pending={<Task pending name='Task-5' coro=<me_coro() running at D:\GB\pythonProject\asyncio\Chapter_5_Asyncio_basics\5_7_asyncio_wait\tmp.py:4> wait_for=<Future pending cb=[Task.task_wakeup()]>>, <Task pending name='Task-4' coro=<me_coro() running at D:\GB\pythonProject\asyncio\Chapter_5_Asyncio_basics\5_7_asyncio_wait\tmp.py:4> wait_for=<Future pending cb=[Task.task_wakeup()]>>, <Task pending name='Task-6' coro=<me_coro() running at D:\GB\pythonProject\asyncio\Chapter_5_Asyncio_basics\5_7_asyncio_wait\tmp.py:4> wait_for=<Future pending cb=[Task.task_wakeup()]>>}
# (2, 3)