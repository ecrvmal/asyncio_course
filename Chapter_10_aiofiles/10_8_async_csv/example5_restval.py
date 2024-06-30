import asyncio

import aiofiles
from aiocsv import AsyncDictReader

async def read_csv_file():
    async with aiofiles.open('students2.csv', mode='r', encoding='utf-8-sig') as afp:
        reader = AsyncDictReader(afp, fieldnames=['Name', 'Surname', 'Age', 'Faculty', 'Average_Grade'], restval='N/A')
        async for row in reader:
            print(row)

asyncio.run(read_csv_file())
