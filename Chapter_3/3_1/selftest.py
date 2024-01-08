import asyncio

async def coocker(i):
    print(f'cooker {i} starts to cook')
    await asyncio.sleep(i)
    print(f'cooker {i} ends to cook')
    return f"dish from coocker {i}"

async def main():
    tasks = [asyncio.create_task(coocker(i)) for i in range(1,4)]
    print(await asyncio.gather(*tasks))


if __name__ == '__main__':
    asyncio.run(main())

