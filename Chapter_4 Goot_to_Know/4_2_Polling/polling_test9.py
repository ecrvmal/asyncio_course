import asyncio

async def polling_function():
    try:
        for i in range(10):
            await asyncio.sleep(1)
            print(f"Polling {i+1}")
    except asyncio.CancelledError:
        print("Polling прерван")

async def interrupt_function():
    await asyncio.sleep(5)
    print("Прерывание выполнено")

async def main():
    task = asyncio.create_task(polling_function())
    await interrupt_function()
    task.cancel()

asyncio.run(main())

