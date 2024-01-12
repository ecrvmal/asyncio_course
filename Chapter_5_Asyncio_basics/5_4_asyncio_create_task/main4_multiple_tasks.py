import asyncio

async def my_task(num_task):
    print(f"Task {num_task} started ")
    await asyncio.sleep(3)
    print(f"Task {num_task} finished")

async def main():
    tasks = []
    for i in range(5):
        task = asyncio.create_task(my_task(i))
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(main())
