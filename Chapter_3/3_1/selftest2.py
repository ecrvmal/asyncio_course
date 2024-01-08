import asyncio


async def coocker(n):
    print(f'coocker {n} starts to coock')
    await asyncio.sleep(n)
    print(f'coocker {n} ends to coock')
    return f'this is dish from coocker {n} '


async def main():
    tasks = [asyncio.create_task(coocker(i)) for i in range(1, 4)]
    print(await asyncio.gather(*tasks))


if __name__ == '__main__':
    asyncio.run(main())