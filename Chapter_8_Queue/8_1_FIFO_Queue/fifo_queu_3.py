import asyncio


async def producer(queue):                                       # объявление асинхронной функции producer, принимающей аргумент queue
    for i in range(5):
        item = f'Элемент {i}'                                    # создание строки с элементом и его номером
        await queue.put(item)                                    # добавление элемента в очередь
        print(f'producer добавил "в" очередеь элемент: {item}')  # вывод сообщения о добавлении элемента в очередь


async def consumer(queue):                                       # объявление асинхронной функции consumer, принимающей аргумент queue
    while True:
        item = await queue.get()                                 # получение элемента из очереди
        print(f'consumer получил "из" очереди элемент: {item}')
        if item is None:                                         # если элемент равен None
            break                                                # выход из цикла
          # вывод сообщения о получении элемента из очереди


async def main():                                                # объявление функции main
    queue = asyncio.Queue()                                      # создание очереди

    # создание задачи для функции producer и consumer
    prod_task = asyncio.create_task(producer(queue))
    cons_task = asyncio.create_task(consumer(queue))
    await prod_task                                             # ожидание завершения задачи для функции producer
    await queue.put(None)                                       # добавление элемента None в очередь для выхода из цикла
    await cons_task                                             # ожидание завершения задачи для функции consumer


asyncio.run(main())