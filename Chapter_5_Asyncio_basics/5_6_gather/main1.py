import asyncio

async def call_api(message : str, result : int, delay : int =2 ):
    print(f'{message} started')
    await asyncio.sleep(delay)
    print(f'{message} ended')
    return result


async def main():
    a, b = await asyncio.gather(call_api('coro1 runs', 5, delay = 3 ),
                                call_api('coro2 runs', 3, delay = 2,)
                                )
    print(f'{a=} \n {b=}')


asyncio.run(main())
