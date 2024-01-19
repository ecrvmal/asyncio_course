import asyncio


async def my_coro():
    print("Корутина запустилась")
    await asyncio.sleep(5)
    print("Корутина завершилась")
    return 42


async def main() -> None:
    print('main started')
    task = asyncio.create_task(my_coro())
    await asyncio.sleep(1)
    print('main continues work')
    try:
        await asyncio.wait_for(task, timeout=1)
        result = task.result()
    except asyncio.TimeoutError :
        print(' the task wasn"t completed in time')
    # print(f'{task.result()=}')

asyncio.run(main())
