import asyncio

event = asyncio.Event()

async def sensor(n, ip):
    await asyncio.sleep(n/10)
    print(f'Датчик {n} IP-адрес {ip} настроен и ожидает срабатывания')
    await event.wait()
    print(f'Датчик {n} IP-адрес {ip} активирован, "Wee-wee-wee-wee"')

async def run_event():
    await asyncio.sleep(5)
    # # наступило событие asyncio.Event()
    print(f'Датчики зафиксировали движение')
    event.set()

async def main():
    ip : list = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]
    tasks: list = []
    for i, i_ip in enumerate(ip):
        tasks.append(asyncio.create_task(sensor(i, i_ip)))

    tasks.append(asyncio.create_task(run_event()))
    await asyncio.gather(*tasks)

    # await asyncio.create_task(run_event())


asyncio.run(main())

#
# Датчик 0 IP-адрес 192.168.0.3 настроен и ожидает срабатывания
# Датчик 1 IP-адрес 192.168.0.1 настроен и ожидает срабатывания
# Датчик 2 IP-адрес 192.168.0.2 настроен и ожидает срабатывания
# Датчик 3 IP-адрес 192.168.0.4 настроен и ожидает срабатывания
# Датчик 4 IP-адрес 192.168.0.5 настроен и ожидает срабатывания
# Датчики зафиксировали движение
# Датчик 0 IP-адрес 192.168.0.3 активирован, "Wee-wee-wee-wee"
# Датчик 1 IP-адрес 192.168.0.1 активирован, "Wee-wee-wee-wee"
# Датчик 2 IP-адрес 192.168.0.2 активирован, "Wee-wee-wee-wee"
# Датчик 3 IP-адрес 192.168.0.4 активирован, "Wee-wee-wee-wee"
# Датчик 4 IP-адрес 192.168.0.5 активирован, "Wee-wee-wee-wee"

