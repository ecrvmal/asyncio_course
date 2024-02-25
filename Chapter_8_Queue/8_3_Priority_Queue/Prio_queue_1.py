import asyncio


async def task(name, priority, queue):                                  # объявление функции task с параметрами (name, priority, queue)
    await queue.put((priority, name))                                   # добавление задачи с приоритетом в очередь
    print(f"{name}, добавлен в очередь, с приоритетом {priority}")      # вывод сообщения о добавлении задачи в очередь


async def main():                                                      # объявление главной асинхронной фунции
    queue = asyncio.PriorityQueue(maxsize=10)                          # создание очереди с максимальным размером 10
    await task("Задача 1", 1, queue)                                  # добавление задачи 1 с приоритетом 1 в очередь
    await task("Задача 2", 3, queue)                                   # добавление задачи 2 с приоритетом 3 в очередь
    await task("Задача 3", 2, queue)                                   # добавление задачи 3 с приоритетом 2 в очередь
    await task("Задача 4", 2, queue)                                   # добавление задачи 4 с приоритетом 2 в очередь
    while not queue.empty():                                           # пока очередь не пуста
        priority, name = await queue.get()                             # получение задачи с наибольшим приоритетом из очереди
        print(f"{name}, с приоритетом {priority} выполняется")         # вывод сообщения о выполнении задачи с указанием ее приоритета

asyncio.run(main())