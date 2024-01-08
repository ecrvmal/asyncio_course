import asyncio

async def counter():
    for i in range(100):
        await asyncio.sleep(.1)
        print(i)


async def main():
    print('we started')
    # await asyncio.sleep(1)
    # await counter()              # non-parallel, occupies 10 seconds

    # tasks = [asyncio.create_task(counter()),]  # non-parallel, occupies 10 seconds
    # await asyncio.gather(*tasks)

    await asyncio.create_task(counter())    # non-parallel, occupies 10 seconds

    print('we completed')


if __name__ == "__main__":
    asyncio.run(main())


# reult:
# we started
# 0
# 1
# 2
# 3
# 4
# .......
# 97
# 98
# 99
# we completed
#
# Process finished with exit code 0
