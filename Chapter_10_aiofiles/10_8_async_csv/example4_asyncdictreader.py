import asyncio

import aiofiles
from aiocsv import AsyncDictReader

async def read_csv_file():
    async with aiofiles.open('students.csv', mode='r', encoding='utf-8-sig') as afp:
        reader = AsyncDictReader(afp, fieldnames=['Name', 'Surname', 'Age', 'Faculty', 'Average_Grade'], restval='N/A')
        async for row in reader:
            print(row)

asyncio.run(read_csv_file())

# C:\Users\VMAL\AppData\Local\Programs\Python\Python311\python.exe D:/GB/pythonProject/asyncio/Chapter_10_aiofiles/10_8_async_csv/example4_asyncdictreader.py
# {'Name': 'Name', 'Surname': 'Surname', 'Age': 'Age', 'Faculty': 'Faculty', 'Average_Grade': 'Average_Grade'}
# {'Name': 'Alice', 'Surname': 'Brown', 'Age': '23', 'Faculty': 'Mathematics', 'Average_Grade': '3.26'}
# {'Name': 'Mary', 'Surname': 'Brown', 'Age': '23', 'Faculty': 'Engineering', 'Average_Grade': '4.45'}
# {'Name': 'Mary', 'Surname': 'White', 'Age': '19', 'Faculty': 'Computer Science', 'Average_Grade': '3.11'}
# {'Name': 'Mary', 'Surname': 'White', 'Age': '20', 'Faculty': 'Biology', 'Average_Grade': '4.26'}
# {'Name': 'James', 'Surname': 'Taylor', 'Age': '19', 'Faculty': 'Physics', 'Average_Grade': '3.79'}
# {'Name': 'Alice', 'Surname': 'Smith', 'Age': '25', 'Faculty': 'Computer Science', 'Average_Grade': '4.64'}
# {'Name': 'Mary', 'Surname': 'Johnson', 'Age': '18', 'Faculty': 'Biology', 'Average_Grade': '3.44'}
# {'Name': 'Alice', 'Surname': 'Brown', 'Age': '20', 'Faculty': 'Physics', 'Average_Grade': '2.39'}
# {'Name': 'Robert', 'Surname': 'White', 'Age': '19', 'Faculty': 'Physics', 'Average_Grade': '3.78'}
# {'Name': 'Robert', 'Surname': 'Smith', 'Age': '25', 'Faculty': 'Engineering', 'Average_Grade': '2.08'}
#
# Process finished with exit code 0


