import asyncio
from random import randint

glob_dict = {}

async def gen_num():
    global glob_dict
    while True:
        await asyncio.sleep(1)
        num = randint(2,6)
        fact=1
        for i in range(1,num+1):
            fact *=i
        glob_dict[num] = fact
        print(f'calculated {fact=}')


async def print_dict():
    global glob_dict
    while True:
        if glob_dict:
            for k in glob_dict.keys():
                key = k
            val = glob_dict.pop(key)
            print (f'removed {key=}, {val=}')
        await asyncio.sleep (0.25)

async def main():
    task1 = asyncio.create_task(print_dict())
    task2 = asyncio.create_task(gen_num())
    await task1
    await task2

asyncio.run(main())