import asyncio

class Update:
    lock = asyncio.Lock()
    shared_resource=0

    async def update_resource(self):
        print(f'Начинаем обновление shared_resource')
        await __class__.lock.acquire()
        temp = __class__.shared_resource
        await asyncio.sleep(1)
        __class__.shared_resource = temp + 1
        __class__.lock.release()
        print(f'Обновление shared_resource завершено-{__class__.shared_resource}')

async def main():
    await asyncio.gather(*[Update().update_resource() for _ in range(2)])
    print(f'shared_resource: {Update.shared_resource}')

asyncio.run(main())