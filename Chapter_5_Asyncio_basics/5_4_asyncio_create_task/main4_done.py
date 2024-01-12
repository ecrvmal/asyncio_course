import asyncio

async def my_task(num_task):
    print(f"Task {num_task} started ")
    await asyncio.sleep(3)
    print(f"Task {num_task} finished")

async def main():
    task1 = asyncio.create_task(my_task(1), name='Task 1')
    task2 = asyncio.create_task(my_task(2), name='Task 2')
    await asyncio.gather(task1, task2)

    if task1.done():
        print("Task 1 is done")
    else:
        print("Task 1 is not done")

    if task2.done():
        print("Task 2 is done")
    else:
        print("Task 2 is not done")

asyncio.run(main())