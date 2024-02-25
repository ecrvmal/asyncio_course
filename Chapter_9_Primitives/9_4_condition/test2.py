import asyncio
import time

storage: int = 0

items_produced: int =0

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}


async def gather_wood(storage_condition, stop_production):
    global storage
    # print(f'starting wood production')
    # Код по добыче 2ед древесины в секунду
    while True:
        async with storage_condition:
            # await storage_condition.wait()
            # await storage_condition.acquire()
            if stop_production.is_set():
                # print('all goods has been produced')
                return
            await asyncio.sleep(1)
            storage += 2
            print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
            storage_condition.notify_all()
            # storage_condition.notify()
            # storage_condition.release()

async def craft_item(storage_condition, stop_production, wood_item, qty):
    global items_produced
    global storage
     # Код изготовлению деревянных предметов
    # print(f'factory got order for {wood_item=}, {qty=}')
    while True:
        async with storage_condition:
            await storage_condition.wait()
            # await storage_condition.acquire()
            if storage >= qty:
                # await asyncio.sleep(0.5)
                print(f'Изготовлен {wood_item}.')
                storage -= qty
                items_produced += 1
                if items_produced == 3:
                    stop_production.set()
                return

            # storage_condition.notify()

async def main():
    storage_condition = asyncio.Condition()
    stop_production = asyncio.Event()
    goods = [asyncio.create_task(craft_item(storage_condition, stop_production, el, qty)) for el, qty in wood_resources_dict.items()]
    await asyncio.gather(gather_wood(storage_condition, stop_production), *goods)

asyncio.run(main())







