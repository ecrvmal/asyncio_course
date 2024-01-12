import asyncio


async def activate_portal(x_time):
    print(f'Активация портала в процессе, требуется времени: {x_time} единиц')
    await asyncio.sleep(x_time)
    return x_time * 2


async def perform_teleportation(x_time):
    print(f'Телепортация в процессе, требуется времени: {x_time} единиц')
    await asyncio.sleep(x_time)
    return x_time + 2

async def recharge_portal(x_time):
    print(f'Подзарядка портала, требуется времени: {x_time} единиц')
    await asyncio.sleep(x_time)
    return x_time * 3

async def check_portal_stability(x_time):
    print(f'Проверка стабильности портала, требуется времени: {x_time} единиц')
    await asyncio.sleep(x_time)
    return x_time + 4

async def restore_portal(x_time):
    print(f'Восстановление портала, требуется времени: {x_time} единиц')
    await asyncio.sleep(x_time)
    return x_time * 5

async def close_portal(x_time):
    print(f'Закрытие портала, требуется времени: {x_time} единиц')
    await asyncio.sleep(x_time)
    return x_time - 1


async def portal_operator():
    activation = asyncio.ensure_future(activate_portal(2))
    teleportation = asyncio.ensure_future(perform_teleportation(3))
    recharging = asyncio.ensure_future(recharge_portal(4))
    checking  = asyncio.ensure_future(check_portal_stability(5))
    restoring = asyncio.ensure_future(restore_portal(6))
    closure = asyncio.ensure_future(close_portal(7))
    tasks = [activation, teleportation, recharging, checking, restoring, closure]
    await asyncio.gather(*tasks)

    print(f'Результат активации портала: {activation.result()} единиц энергии')
    print(f'Результат телепортации: {teleportation.result()} единиц времени')
    print(f'Результат подзарядки портала: {recharging.result()} единиц энергии')
    print(f'Результат проверки стабильности: {checking.result()} единиц времени')
    print(f'Результат восстановления портала: {restoring.result()} единиц энергии')
    print(f'Результат закрытия портала: {closure.result()} единиц времени')


asyncio.run(portal_operator())