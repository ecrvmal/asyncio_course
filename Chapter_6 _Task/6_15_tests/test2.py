import asyncio
import random


async def scan_port(address, port):
    value = random.choice([True, False])
    await asyncio.sleep(2)
    if value:
        print(f'Порт {port} на адресе 192.168.0.1 открыт')
        return port


async def scan_range(address, start_port, end_port):
    print(f'Сканирование портов с {start_port} по {end_port} на адресе {address}')
    tasks = [asyncio.create_task(scan_port(address, port_num)) for port_num in range(start_port, end_port+1)]
    results = await asyncio.gather(*tasks)
    if results:
        filtered_results = list(filter(lambda x: bool(x), results))
        print(f'Открытые порты на адресе {address}: {filtered_results}')
    else:
        print(f'Открытых портов на адресе {address} не найдено')


asyncio.run(scan_range('192.168.0.1', 80, 85))
