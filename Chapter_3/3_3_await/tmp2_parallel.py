import asyncio

async def counter():
    for i in range(100):
        await asyncio.sleep(.1)
        print(i)

async def informer():
    print('we started')
    await asyncio.sleep(1)
    print('we completed')


async def main():

    tasks = [asyncio.create_task(informer()),
             asyncio.create_task(counter()),
             ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

# result
#
# we started
# 0
# 1
# ...
# 8
# we completed
# 9
# 10
# 11
# .....
# 97
# 98
# 99
#
# Process finished with exit code 0