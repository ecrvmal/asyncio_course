import asyncio

async def eternity():
    # Засыпаем на 1 час
    await asyncio.sleep(3600)
    print('Ура!')

async def main():
    # ждем не более 1 сек.
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())