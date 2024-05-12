import asyncio


# Корутина worker, принимающая объект asyncio.Barrier.
async def worker(barrier: asyncio.Barrier, num):
    await asyncio.sleep(num)
    print(f"worker_{num} ждет на барьере")

    # В этой точке выполнение задачи приостанавливается
    # до момента накопления на барьере заданного количества задач.
    await barrier.wait()
    # После преодоления барьера работа задачи возобновляется.

    await asyncio.sleep(0.5)
    # Вывод сообщения о прохождении барьера worker-ом.
    print(f"worker_{num} прошел барьер")


async def main():
    # Создание объекта asyncio.Barrier (для разблокировки ожидаем 4 задачи).
    barrier = asyncio.Barrier(4)
    tasks = [asyncio.create_task(worker(barrier, num)) for num in range(3)]

    print(f'Состояние {barrier=}')
    print("Ждем, пока worker's пройдут барьер")
    await asyncio.sleep(0)
    print(f'Состояние {barrier=}')
    # Регистрируем на нашем барьере последнюю, 4-ю задачу для преодоления барьера.

    await asyncio.sleep(6)
    print("4-я задача достигла барьера")
    await barrier.wait()

    # Часть кода которая может быть выполнена только после преодоления барьера.
    # Имитация выполнения длительной I/O операции.
    await asyncio.sleep(1)
    print("Все задачи успешно прошли барьер")
    print(f'Состояние {barrier=}')


asyncio.run(main())

#
# output listing:
# C:\Users\VMAL\AppData\Local\Programs\Python\Python311\python.exe "D:/GB/pythonProject/asyncio/Chapter_9_Primitives/Барьер для защиты доступа  Barrier/example1.py"
# Состояние barrier=<asyncio.locks.Barrier object at 0x00000282EDE929D0 [filling, waiters:0/4]>
# Ждем, пока worker's пройдут барьер
# Состояние barrier=<asyncio.locks.Barrier object at 0x00000282EDE929D0 [filling, waiters:0/4]>
# worker_0 ждет на барьере
# worker_1 ждет на барьере
# worker_2 ждет на барьере
# 4-я задача достигла барьера
# worker_0 прошел барьер
# worker_1 прошел барьер
# worker_2 прошел барьер
# Все задачи успешно прошли барьер
# Состояние barrier=<asyncio.locks.Barrier object at 0x00000282EDE929D0 [filling, waiters:0/4]>
#
# Process finished with exit code 0

