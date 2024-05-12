# дописать корутину main(), которая создаст задачу для корутины coroutine() и запланирует её выполнение.
# Корутина main() должна дождаться результата от корутины coroutine() и напечатать его,
# когда результат станет доступен.

import asyncio
from random import randint



async def coroutine():
    number = randint(1, 7)
    await asyncio.sleep(number)
    return number


async def main():
    task = asyncio.create_task(coroutine())
    await task
    result = task.result()
    print(result)


asyncio.run(main())