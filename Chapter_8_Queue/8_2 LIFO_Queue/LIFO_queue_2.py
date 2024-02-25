import asyncio


async def worker(name, lifo_queue):
    while True:
        task = await lifo_queue.get()                    # Получаем задание из очереди
        print(f"Рабочий_{name}. получил задачу: {task}")
        await asyncio.sleep(0.5)                         # Обрабатываем задание
        print(lifo_queue.qsize())
        # if name != "1":
        lifo_queue.task_done()                           # Отправляем сигнал, что задание выполнено


async def main():
    lifo_queue = asyncio.LifoQueue()                      # Создаем очередь
    for i in range(10):
        await lifo_queue.put(i)                           # Заполняем очередь заданиями

    workers = [asyncio.create_task(worker(f"{i}", lifo_queue)) for i in range(3)]  # Создаем несколько задач-рабочих
    await lifo_queue.join()                               # Ждем, пока все задания не будут выполнены
    for w in workers:                                     # Останавливаем задачи-рабочие
        w.cancel()


if __name__ == "__main__":
    asyncio.run(main())