import asyncio

async def task_func():
    print("Задача выполнена")  # Вывод сообщения о выполнении задачи
    return "Результат задачи"  # Возвращение результата задачи

async def main():
    task = asyncio.create_task(task_func())                 # Создаем задачу
    _, pending = await asyncio.wait({task})                 # Ожидаем завершения задачи
    assert not pending, f"{len(pending)} ожидающих задач"   # Проверяем, что задача завершена
    print("Результат задачи:", task.result())               # Вывод результата задачи

asyncio.run(main())  # Запуск главной функции

# output:
# Задача выполнена
# Результат задачи: Результат задачи
