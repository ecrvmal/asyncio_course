import asyncio
from multiprocessing import Process, Queue


async def producer(queue):
    for i in range(5):
        print(f"Произведено: {i}")
        await asyncio.sleep(1)
        queue.put(i)
    queue.put(None)  # Отправка сигнала о завершении


async def consumer(queue):
    while True:
        item = queue.get()
        if item is None:  # Признак завершения
            break
        print(f"Потреблено: {item}")
        await asyncio.sleep(1)


def run_producer(queue):
    asyncio.run(producer(queue))


def run_consumer(queue):
    asyncio.run(consumer(queue))


if __name__ == "__main__":
    queue = Queue()

    producer_process = Process(target=run_producer, args=(queue,))
    consumer_process = Process(target=run_consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    