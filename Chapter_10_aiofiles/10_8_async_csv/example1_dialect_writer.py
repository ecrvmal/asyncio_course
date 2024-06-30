import csv
import asyncio
import aiofiles
from aiocsv import AsyncWriter
from datetime import datetime


class CustomDialect(csv.Dialect):
    delimiter = '+'
    quotechar = '/'
    doublequote = False
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL

csv.register_dialect('customDialect', CustomDialect)

async def write_row(writer, row):
    await writer.writerow(row)

async def print_time():
    print(f"Current Time: {datetime.now()}")

async def main():
    async with aiofiles.open("test_Dialect.csv", mode="w", encoding="utf-8", newline="") as afp:
        writer = AsyncWriter(afp, dialect='customDialect')
        data = [["Column1", "Column2", "Column3", "Column4", "Column5"]]  # replace with your data
        data += [["Data1", "Data2", "Data3", "Data4", str(i)] for i in range(1, 101)]  # add 100 rows
        for row in data:
            await write_row(writer, row)
            await print_time()

asyncio.run(main())

