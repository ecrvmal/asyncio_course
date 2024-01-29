import asyncio
import random

async def scan_port(address, port):
    value = random.randint(1, 100) == 1
    await asyncio.sleep(1)
    if value:
        print(f"Port {port} on {address} is open")
        return port


async def scan_range(address, start_port, end_port):
    print(f"Scanning ports {start_port}-{end_port} on {address}")
    tasks = [asyncio.create_task(scan_port(address, port_num)) for port_num in range(start_port, end_port+1)]
    results = await asyncio.gather(*tasks)
    filtered_results = list(filter(lambda x: bool(x), results))
    if filtered_results:
        # print(f'at {address=} open ports = {len(filtered_results)}')
        return address, len(filtered_results)
    else:
        print(f"No open ports on {address}")
        return address, 0


async def main():
    number_open_ports = {}
    # список ip-адресов
    ip_addresses = [
        '192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4',
        '192.168.0.5', '192.168.0.6', '192.168.0.7', '192.168.0.8',
        '192.168.0.9', '192.168.0.10', '192.168.1.1', '192.168.1.2',
        '192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6',
        '192.168.1.7', '192.168.1.8', '192.168.1.9', '192.168.1.10',
        '192.168.2.1', '192.168.2.2', '192.168.2.3', '192.168.2.4',
        '192.168.2.5'
    ]

    start_port = 0 # Получение стартового порта из аргументов командной строки
    end_port = 300 # Получение конечного порта из аргументов командной строки
    tasks = [asyncio.create_task(scan_range(ip_address, start_port, end_port))
                                for ip_address in ip_addresses]
    # Выполнение асинхронной функции сканирования портов
    result = await asyncio.gather(*tasks)
    for el in result:
        print(f"Всего найдено открытых портов {el[1]} для ip: {el[0]}")

asyncio.run(main()) # Запуск асинхронного приложения
