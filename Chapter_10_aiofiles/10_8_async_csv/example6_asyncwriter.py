import asyncio
import aiofiles
from aiocsv import AsyncWriter

async def write_csv_file():
    async with aiofiles.open("new_file.csv", mode="w", encoding="utf-8", newline="") as afp:
        writer = AsyncWriter(afp)
        await writer.writerows([
            ["John", 26],
            ["Sasha", 42],
            ["Hana", 37]
        ])

asyncio.run(write_csv_file())

# Output: file
# John,26
# Sasha,42
# Hana,37



