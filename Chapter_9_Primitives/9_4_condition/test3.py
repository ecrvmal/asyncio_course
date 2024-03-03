import asyncio

stone_material = 0
metal_material = 0
cloth_material = 0
stone_items = 0
metal_items = 0
cloth_items = 0


async def gather_stone(stone_condition, stone_completed):
    # Добываем камень, 10ед каждую сек.
    global stone_material
    # print(f'Raw stone started')
    while True:
        if stone_completed.is_set():
            # print(f'stop stone production')
            return
        async with stone_condition:
            await asyncio.sleep(1)
            stone_material += 10
            # print(f'Stone stock: {stone_material} units')
            print(f'Добыто 10 ед. камня. На складе {stone_material} ед.')
            stone_condition.notify_all()
            await stone_condition.wait()



async def gather_metal(metal_condition, metal_completed):
    # Добываем металл, 6ед каждую сек.
    global metal_material
    # print(f'Raw metal started')
    while True:
        if metal_completed.is_set():
            # print(f'stop metal production')
            return
        async with metal_condition:
            await asyncio.sleep(1)
            metal_material += 6
            # print (f'Metal stock: {metal_material} units')
            print(f'Добыто 6 ед. металла. На складе {metal_material} ед.')
            metal_condition.notify_all()
            await metal_condition.wait()


async def gather_cloth(cloth_condition, cloth_completed):
    # Добываем ткань, 8ед каждую сек.
    global cloth_material
    # print(f'Raw cloth started')
    while True:
        if cloth_completed.is_set():
            # print(f'stop cloth production')
            return
        async with cloth_condition:
            await asyncio.sleep(1)
            cloth_material += 8
            # print(f'cloth stock: {cloth_material} units')
            print(f'Добыто 8 ед. ткани. На складе {cloth_material} ед.')
            cloth_condition.notify_all()
            await cloth_condition.wait()


async def craft_stone_items(stone_condition, stone_completed, item, qty):
    # Мастерская по крафту из камня
    global stone_items
    global stone_material
    # print(f'Stone order for {item}, need {qty}')
    while True:
        async with stone_condition:
            await stone_condition.wait()
            if stone_material >= qty:
                # print(f'item {item} was produced')
                print(f'Изготовлен {item} из камня.')
                stone_material -= qty
                stone_items += 1
                if stone_items == 3:
                    stone_completed.set()
                    # print(f'all stone goods were produced')
                    stone_condition.notify()
                return
            else:
                stone_condition.notify()


async def craft_metal_items(metal_condition, metal_completed, item, qty):
    # Мастерская по крафту из мателла
    global metal_items
    global metal_material
    # print(f'Metal order for {item}, need {qty}')
    while True:
        async with metal_condition:
            await metal_condition.wait()
            if metal_material >= qty:
                # print(f'item {item} was produced')
                print(f'Изготовлен {item} из металла.')
                metal_material -= qty
                metal_items += 1
                if metal_items == 3:
                    metal_completed.set()
                    # print(f'all metal goods were produced')
                    metal_condition.notify()
                return
            else:
                metal_condition.notify_all()


async def craft_cloth_items(cloth_condition, cloth_completed, item, qty):
    # Мастерская по крафту из ткани
    global cloth_items
    global cloth_material
    # print(f'Cloth order for {item}, need {qty}')
    while True:
        async with cloth_condition:
            await cloth_condition.wait()
            if cloth_material >= qty:
                # print(f'item {item} was produced')
                print(f'Изготовлен {item} из ткани.')
                cloth_material -= qty
                cloth_items += 1
                if cloth_items == 3:
                    cloth_completed.set()
                    # print(f'all cloth goods were produced')
                    cloth_condition.notify()
                return
            else:
                cloth_condition.notify_all()


async def main():
    stone_condition = asyncio.Condition()
    stone_completed = asyncio.Event()
    metal_condition = asyncio.Condition()
    metal_completed = asyncio.Event()
    cloth_condition = asyncio.Condition()
    cloth_completed = asyncio.Event()


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

    stone_goods = [asyncio.create_task(craft_stone_items(stone_condition, stone_completed, name, qty)) for name, qty in stone_resources_dict.items()]
    metal_goods = [asyncio.create_task(craft_metal_items(metal_condition, metal_completed, name, qty)) for name, qty in metal_resources_dict.items()]
    cloth_goods = [asyncio.create_task(craft_cloth_items(cloth_condition, cloth_completed, name, qty)) for name, qty in cloth_resources_dict.items()]

    await asyncio.gather(gather_stone(stone_condition, stone_completed),
                         gather_metal(metal_condition, metal_completed),
                         gather_cloth(cloth_condition, cloth_completed),
                         *stone_goods, *metal_goods, *cloth_goods)

asyncio.run(main())



