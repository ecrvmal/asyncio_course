import asyncio

async def my_coro():
    print("start 5-sec task")
    await asyncio.sleep(5)
    print("end 5-sec task")

async def main():
    task = asyncio.create_task(my_coro())
    try:
        await asyncio.wait_for(task, timeout=3)
    except asyncio.TimeoutError:
        print("Задача не была завершена в установленное время")

asyncio.run(main())