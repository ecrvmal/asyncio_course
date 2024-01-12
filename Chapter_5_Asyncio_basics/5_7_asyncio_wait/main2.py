import asyncio

async def task_func(task_id):
    print(f"Задача {task_id} выполнена")  # Выводим сообщение о выполнении задачи
    return f"Результат задачи {task_id}"  # Возвращаем результат задачи

async def main():
    tasks = [asyncio.create_task(task_func(i)) for i in range(5)]    # Создаем несколько задач
    _, pending = await asyncio.wait(tasks)                           # Ожидаем завершения всех задач
    assert not pending, f"{len(pending)} ожидающих задач"            # Проверяем, что все задачи завершены
    for task in tasks:
        print(f"Результат задачи {task.get_coro()}:", task.result()) # Выводим результат каждой задачи

asyncio.run(main())

#
# output:
# Задача 0 выполнена
# Задача 1 выполнена
# Задача 2 выполнена
# Задача 3 выполнена
# Задача 4 выполнена
# Результат задачи <coroutine object task_func at 0x000001EA37CE7A00>: Результат задачи 0
# Результат задачи <coroutine object task_func at 0x000001EA37CE7920>: Результат задачи 1
# Результат задачи <coroutine object task_func at 0x000001EA37CE7AE0>: Результат задачи 2
# Результат задачи <coroutine object task_func at 0x000001EA37CE7840>: Результат задачи 3
# Результат задачи <coroutine object task_func at 0x000001EA37CE7CA0>: Результат задачи 4
