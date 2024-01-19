import asyncio

async def my_task(number):
    current_task = asyncio.current_task()
    print(
        f"Задача {number} стартовала. Текущий объект задачи: {current_task}")
    await asyncio.sleep(1)
    print(f"Задача {number} выполнена")

async def main():
    task1 = asyncio.create_task(my_task(1))
    task2 = asyncio.create_task(my_task(2))
    print('ha-ha')
    await asyncio.gather(task1, task2)


asyncio.run(main())

# output:
# ha-ha
# Задача 1 стартовала. Текущий объект задачи: <Task pending name='Task-2' coro=<my_task() running at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_5_current_task\main1.py:6> cb=[gather.<locals>._done_callback() at C:\Users\VMAL\AppData\Local\Programs\Python\Python310\lib\asyncio\tasks.py:720]>
# Задача 2 стартовала. Текущий объект задачи: <Task pending name='Task-3' coro=<my_task() running at D:\GB\pythonProject\asyncio\Chapter_6 _Task\6_5_current_task\main1.py:6> cb=[gather.<locals>._done_callback() at C:\Users\VMAL\AppData\Local\Programs\Python\Python310\lib\asyncio\tasks.py:720]>
# Задача 1 выполнена
# Задача 2 выполнена
