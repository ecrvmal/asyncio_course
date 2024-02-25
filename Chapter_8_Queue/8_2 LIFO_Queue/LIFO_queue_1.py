import asyncio

async def lifoqueue_example():
    lifo_queue = asyncio.LifoQueue(maxsize=3)       # создание LifoQueue с максимальным количеством элементов 3

    # добавление элементов в очередь
    await lifo_queue.put("Первый элемент")
    await lifo_queue.put("Второй элемент")
    await lifo_queue.put("Третий элемент")

    last_item = await lifo_queue.get()              # получение последнего элемента из очереди
    print(last_item)

    second_last_item = await lifo_queue.get()       # получение второго с конца элемента из очереди
    print(second_last_item)

    first_item = await lifo_queue.get()             # получение первого элемента из очереди
    print(first_item)


asyncio.run(lifoqueue_example())                    # запуск примера