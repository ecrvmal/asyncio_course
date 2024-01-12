import asyncio


async def activate_portal(x_time):
    print(f'Активация портала в процессе, требуется времени: {x_time} единиц')
    await asyncio.sleep(x_time)
    return x_time * 2


async def perform_teleportation(x_time):
    print(f'Телепортация в процессе, требуется времени: {x_time} единиц')
    await asyncio.sleep(x_time)
    return x_time + 2


async def portal_operator():
    activation = await asyncio.ensure_future(activate_portal(2))
    if activation > 4:
        activation = 1
    teleportation = await asyncio.ensure_future(perform_teleportation(activation))
    print(f'Результат активации портала: {activation} единиц энергии')
    print(f'Результат телепортации: {teleportation} единиц времени')


asyncio.run(portal_operator())