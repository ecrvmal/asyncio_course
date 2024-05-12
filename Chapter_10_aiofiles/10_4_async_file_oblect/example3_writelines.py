# Вот пример использования f.writelines(lines):

import asyncio
import aiofiles

async def main():
    lines = ['Hello, world!\n', 'How are you?\n', 'Goodbye!\n']
    async with aiofiles.open('myfile.txt', mode='w') as f:
        await f.writelines(lines)

asyncio.run(main())


