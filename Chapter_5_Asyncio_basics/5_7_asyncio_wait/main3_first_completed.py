import asyncio

async def foo():
    print("Запущена корутина foo")
    await asyncio.sleep(5)
    print("Явное переключение контекста обратно на 'foo'")

async def bar():
    print("Запущена корутина bar")
    await asyncio.sleep(3)
    print("Явное переключение контекста обратно на 'bar'")

async def main():
    tasks = [asyncio.create_task(foo()), asyncio.create_task(bar())]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print("Задание завершено: ", task)
    for task in pending:
        print("Задание ожидает выполнения: ", task)
    print('-' * 20)

    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    # for task in done:
    #     print("Задание завершено: ", task)
    # for task in pending:
    #     print("Задание ожидает выполнения: ", task)


    # await asyncio.gather(*tasks)


asyncio.run(main())

# output:
# Запущена корутина foo
# Запущена корутина bar
# Явное переключение контекста обратно на 'bar'
# Задание завершено:  <Task finished name='Task-3' coro=<bar() done, defined at D:\GB\pythonProject\asyncio\Chapter_5_Asyncio_basics\5_7_asyncio_wait\main3_first_completed.py:8> result=None>
# Задание ожидает выполнения:  <Task pending name='Task-2' coro=<foo() running at D:\GB\pythonProject\asyncio\Chapter_5_Asyncio_basics\5_7_asyncio_wait\main3_first_completed.py:5> wait_for=<Future pending cb=[Task.task_wakeup()]>>
# --------------------
# Явное переключение контекста обратно на 'foo'
# Задание завершено:  <Task finished name='Task-3' coro=<bar() done, defined at D:\GB\pythonProject\asyncio\Chapter_5_Asyncio_basics\5_7_asyncio_wait\main3_first_completed.py:8> result=None>
# Задание завершено:  <Task finished name='Task-2' coro=<foo() done, defined at D:\GB\pythonProject\asyncio\Chapter_5_Asyncio_basics\5_7_asyncio_wait\main3_first_completed.py:3> result=None>
#
# Process finished with exit code 0
