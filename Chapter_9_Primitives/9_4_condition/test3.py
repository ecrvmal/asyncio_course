

import asyncio



stone_condition = asyncio.Condition()
stone_completed = asyncio.Event()
metal_condition = asyncio.Condition()
metal_completed = asyncio.Event()
cloth_condition = asyncio.Condition()
cloth_completed = asyncio.Event()
stone_material = 0
metal_material = 0
cloth_material = 0
stone_items = 0
metal_items = 0
cloth_items = 0



async def gather_stone():
    # Добываем камень, 10ед каждую сек.
    global stone_condition
    global stone_completed
    global stone_material
    print(f'Raw stone started')
    while True:
        if stone_completed:
            print(f'stop stone production')
            return
        async with stone_condition:
            await asyncio.sleep(1)
            stone_material += 10
            print (f'Stone stock: {stone_material} units')
            stone_condition.notify_all()
            await stone_condition.wait()



async def gather_metal():
    # Добываем металл, 6ед каждую сек.
    global metal_condition
    global metal_completed
    global metal_material
    print(f'Raw metal started')
    while True:
        if metal_completed:
            print(f'stop metal production')
            return
        async with metal_condition:
            await asyncio.sleep(1)
            metal_material += 10
            print (f'Metal stock: {metal_material} units')
            metal_condition.notify_all()
            await metal_condition.wait()


async def gather_cloth():
    # Добываем ткань, 8ед каждую сек.
    global cloth_condition
    global cloth_completed
    global cloth_material
    print(f'Raw cloth started')
    while True:
        if cloth_completed:
            print(f'stop cloth production')
            return
        async with cloth_condition:
            await asyncio.sleep(1)
            cloth_material += 8
            print (f'cloth stock: {cloth_material} units')
            cloth_condition.notify_all()
            await cloth_condition.wait()


async def craft_stone_items(item, qty):
    # Мастерская по крафту из камня
    global stone_items
    global stone_condition
    global stone_material
    global stone_completed
    print(f'Stone order for {item}, need {qty}')
    while True:
        async with stone_condition:
            if stone_material >= qty:
                await stone_condition.wait()
                print(f'item {item} was produced')
                stone_material -= qty
                stone_items +=1
                if stone_items == 3:
                    stone_completed.set()
                    print(f'all stone goods were produced')
                return
            stone_condition.notify()



async def craft_metal_items(item, qty):
    # Мастерская по крафту из мателла
    global metal_items
    global metal_condition
    global metal_material
    global metal_completed
    print(f'Metal order for {item}, need {qty}')
    while True:
        async with metal_condition:
            if metal_material >= qty:
                await stone_condition.wait()
                print(f'item {item} was produced')
                metal_material -= qty
                metal_items += 1
                if metal_items == 3:
                    metal_completed.set()
                    print(f'all metal goods were produced')
                return
            metal_condition.notify_all()


async def craft_cloth_items(item, qty):
    # Мастерская по крафту из ткани
    global cloth_items
    global cloth_condition
    global cloth_material
    global cloth_completed
    print(f'Cloth order for {item}, need {qty}')
    while True:
        async with cloth_condition:
            if cloth_material >= qty:
                await cloth_condition.wait()
                print(f'item {item} was produced')
                cloth_material -= qty
                cloth_items += 1
                if cloth_items == 3:
                    cloth_completed.set()
                    print(f'all cloth goods were produced')
                return
            cloth_condition.notify_all()


async def main():
    # Запускаем производства
    stone_resources_dict = {
        'Каменная плитка': 10,
        'Каменная ваза': 40,
        'Каменный столб': 50,
    }

    metal_resources_dict = {
        'Металлическая цепь': 6,
        'Металлическая рамка': 24,
        'Металлическая ручка': 54,
    }

    cloth_resources_dict = {
        'Тканевая занавеска': 8,
        'Тканевый чехол': 24,
        'Тканевое покрывало': 48,
    }

    stone_goods = [asyncio.create_task(craft_stone_items(name, qty)) for name, qty in stone_resources_dict.items()]
    metal_goods = [asyncio.create_task(craft_metal_items(name, qty)) for name, qty in metal_resources_dict.items()]
    cloth_goods = [asyncio.create_task(craft_cloth_items(name, qty)) for name, qty in cloth_resources_dict.items()]

    await asyncio.gather(gather_stone(), gather_metal(), gather_cloth(),
                         *stone_goods, *metal_goods, *cloth_goods)

asyncio.run(main())

