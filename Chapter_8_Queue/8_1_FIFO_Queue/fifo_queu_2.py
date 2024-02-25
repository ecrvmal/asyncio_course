import asyncio

async def read_queue(queue):                        # определяем корутину read_queue, которая будет читать из очереди
    while True:                                     # запускаем бесконечный цикл для чтения элементов из очереди
        item = await queue.get()                    # получаем элемент из очереди
        print("Получен элемент из очереди:", item)  # выводим полученный элемент


async def main():                                   # определяем корутину main, которая будет запускать read_queue и добавлять элементы в очередь
    queue = asyncio.Queue()                         # создаем очередь
    asyncio.create_task(read_queue(queue))          # создаем задачу для корутины read_queue
    await queue.put("Первый элемент")               # добавляем первый элемент в очередь
    await queue.put("Второй элемент")               # добавляем второй элемент в очередь


asyncio.run(main())