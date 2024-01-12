import asyncio

async def my_task(num_task):
    print(f"Task {num_task} started ")
    await asyncio.sleep(3)
    print(f"Task {num_task} finished")

async def test_done(t1, t2):
    while True:
        await asyncio.sleep(0.25)
        if t1.done():
            print("Task 1 is done")
        else:
            print("Task 1 is not done")

        if t2.done():
            print("Task 2 is done")
        else:
            print("Task 2 is not done")

        if t2.done() and t1.done():
            return


async def main():
    task1 = asyncio.create_task(my_task(1), name='Task 1')
    task2 = asyncio.create_task(my_task(2), name='Task 2')
    task3 = asyncio.create_task(test_done(task1, task2), name='Task 3')
    await asyncio.gather(task1, task2, task3)


asyncio.run(main())