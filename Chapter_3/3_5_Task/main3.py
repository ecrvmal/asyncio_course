import asyncio


async def my_task(i):
    if i == 4:
        print(all_tasks := asyncio.all_tasks(), "Всего невыполненных задач в 4:", len(all_tasks))
    print(f"Running task {i}")
    await asyncio.sleep(1)
    print(f"Task {i} complete")



async def main():
    # Убеждаемся, что Task-1 является текущей задачей созданной из main()
    print("Текущая задача:", asyncio.current_task())
    # Убеждаемся, что до создания задач это единственная задача
    print(all_tasks := asyncio.all_tasks(), "Всего невыполненных задач:", len(all_tasks))
    tasks = [asyncio.create_task(my_task(i)) for i in range(5)]
    # После создания задач убеждаемся, что теперь задач 6
    print(all_tasks := asyncio.all_tasks(), "Всего невыполненных задач:", len(all_tasks))

    #  В качестве доказательства того, что задачи запускаются после завершения работы Task-1
    #  такая же команда выполнится при запуске задачи 4.
    #  Невыполненных задач - 5, Task-1 в этом списке задач отсутствует

asyncio.run(main())