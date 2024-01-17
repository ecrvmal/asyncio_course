import asyncio

async def main():
    print("Hello, World!")


loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)

loop.run_until_complete(main())
loop.close()


# Вывод:
#
# Hello, World!