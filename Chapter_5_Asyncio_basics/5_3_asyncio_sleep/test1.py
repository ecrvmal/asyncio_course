# Напишите код, для выполнения трех корутин. Каждая корутина должна выводить два сообщения,
# с задержкой между первым и вторым сообщениями, определенной с помощью await asyncio.sleep().
# Время задержки должно быть разным для каждой корутины,
# чтобы демонстрировать влияние времени сна на порядок выполнения задач.
#
# Sample Output:
#
# Первое сообщение от корутины 1
# Первое сообщение от корутины 2
# Первое сообщение от корутины 3
# Второе сообщение от корутины 3
# Второе сообщение от корутины 2
# Второе сообщение от корутины 1


import asyncio

async def coroutine_1():
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(4)  # Подберите необходимую задержку
    print("Второе сообщение от корутины 1")

async def coroutine_2():
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(3)  # Подберите необходимую задержку
    print("Второе сообщение от корутины 2")

async def coroutine_3():
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(2)  # Подберите необходимую задержку
    print("Второе сообщение от корутины 3")

async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )

asyncio.run(main())