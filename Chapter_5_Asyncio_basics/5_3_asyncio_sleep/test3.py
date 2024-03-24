# Сообщения должны выводиться в следующем порядке:
#
# Сообщение 1 от корутины 1
# Сообщение 1 от корутины 2
# Сообщение 1 от корутины 3
# Сообщение 1 от корутины 4
# Сообщение 1 от корутины 5
# Сообщение 1 от корутины 6
# Сообщение 2 от корутины 1
# Сообщение 2 от корутины 2
# Сообщение 2 от корутины 3
# Сообщение 2 от корутины 4
# Сообщение 2 от корутины 5
# Сообщение 2 от корутины 6

import asyncio

async def coroutine_1():
    await asyncio.sleep(1)  # Задержка для первого сообщения
    print("Сообщение 1 от корутины 1")
    await asyncio.sleep(7)  # Задержка для второго сообщения
    print("Сообщение 2 от корутины 1")

async def coroutine_2():
    await asyncio.sleep(2)
    print("Сообщение 1 от корутины 2")
    await asyncio.sleep(8)
    print("Сообщение 2 от корутины 2")

async def coroutine_3():
    await asyncio.sleep(3)
    print("Сообщение 1 от корутины 3")
    await asyncio.sleep(9)
    print("Сообщение 2 от корутины 3")

async def coroutine_4():
    await asyncio.sleep(4)
    print("Сообщение 1 от корутины 4")
    await asyncio.sleep(10)
    print("Сообщение 2 от корутины 4")

async def coroutine_5():
    await asyncio.sleep(5)
    print("Сообщение 1 от корутины 5")
    await asyncio.sleep(11)
    print("Сообщение 2 от корутины 5")

async def coroutine_6():
    await asyncio.sleep(6)
    print("Сообщение 1 от корутины 6")
    await asyncio.sleep(12)
    print("Сообщение 2 от корутины 6")

async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
        coroutine_4(),
        coroutine_5(),
        coroutine_6(),
    )

asyncio.run(main())

