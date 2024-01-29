# https://stepik.org/lesson/1022249/step/9?unit=1030276
import asyncio

passengers = [
    {"Name": "John", "Age": 25, "Speed": 3, "Job": "Engineer"},
    {"Name": "Sarah", "Age": 32, "Speed": 6, "Job": "Doctor"},
    {"Name": "Mike", "Age": 28, "Speed": 4, "Job": "Teacher"},
    {"Name": "Emma", "Age": 30, "Speed": 3, "Job": "Nurse"},
    {"Name": "Robert", "Age": 45, "Speed": 7, "Job": "Lawyer"},
    {"Name": "Olivia", "Age": 27, "Speed": 3, "Job": "Architect"},
    {"Name": "Charlie", "Age": 35, "Speed": 4, "Job": "Chef"},
    {"Name": "Sophia", "Age": 40, "Speed": 6, "Job": "Scientist"},
    {"Name": "Jacob", "Age": 29, "Speed": 4, "Job": "Photographer"},
    {"Name": "Grace", "Age": 31, "Speed": 6, "Job": "Designer"},
    {"Name": "William", "Age": 34, "Speed": 7, "Job": "Writer"},
    {"Name": "Chloe", "Age": 26, "Speed": 3, "Job": "Journalist"},
    {"Name": "Lucas", "Age": 33, "Speed": 4, "Job": "Pilot"},
    {"Name": "Ella", "Age": 28, "Speed": 4, "Job": "Artist"},
    {"Name": "Ethan", "Age": 37, "Speed": 6, "Job": "Actor"},
    {"Name": "Ava", "Age": 30, "Speed": 4, "Job": "Dancer"},
    {"Name": "Noah", "Age": 32, "Speed": 1, "Job": "Musician"},
    {"Name": "Isabella", "Age": 33, "Speed": 6, "Job": "Singer"},
    {"Name": "Liam", "Age": 31, "Speed": 4, "Job": "Director"},
    {"Name": "Mia", "Age": 29, "Speed": 3, "Job": "Producer"},
    {"Name": "Alexander", "Age": 35, "Speed": 8, "Job": "Engineer"},
    {"Name": "Sophie", "Age": 32, "Speed": 4, "Job": "Doctor"},
    {"Name": "Benjamin", "Age": 28, "Speed": 3, "Job": "Teacher"},
    {"Name": "Emily", "Age": 30, "Speed": 4, "Job": "Nurse"},
    {"Name": "James", "Age": 45, "Speed": 6, "Job": "Lawyer"},
    {"Name": "Amelia", "Age": 27, "Speed": 4, "Job": "Architect"},
    {"Name": "Henry", "Age": 35, "Speed": 3, "Job": "Chef"},
    {"Name": "Jessica", "Age": 40, "Speed": 2, "Job": "Scientist"},
    {"Name": "John", "Age": 25, "Speed": 3, "Job": "Engineer"},
    {"Name": "Sarah", "Age": 32, "Speed": 6, "Job": "Doctor"},
    {"Name": "Mike", "Age": 28, "Speed": 4, "Job": "Teacher"},
    {"Name": "Emma", "Age": 30, "Speed": 3, "Job": "Nurse"},
    {"Name": "Robert", "Age": 45, "Speed": 7, "Job": "Lawyer"},
    {"Name": "Olivia", "Age": 27, "Speed": 3, "Job": "Architect"},
    {"Name": "Charlie", "Age": 35, "Speed": 4, "Job": "Chef"},
    {"Name": "Sophia", "Age": 40, "Speed": 6, "Job": "Scientist"},
    {"Name": "Jacob", "Age": 29, "Speed": 4, "Job": "Photographer"},
    {"Name": "Grace", "Age": 31, "Speed": 6, "Job": "Designer"},
    {"Name": "William", "Age": 34, "Speed": 7, "Job": "Writer"},
    {"Name": "Chloe", "Age": 26, "Speed": 3, "Job": "Journalist"},
    {"Name": "Lucas", "Age": 33, "Speed": 4, "Job": "Pilot"},
    {"Name": "Ella", "Age": 28, "Speed": 8, "Job": "Artist"},
    {"Name": "Ethan", "Age": 37, "Speed": 6, "Job": "Actor"},
    {"Name": "Ava", "Age": 30, "Speed": 4, "Job": "Dancer"},
    {"Name": "Noah", "Age": 32, "Speed": 2, "Job": "Musician"},
    {"Name": "Isabella", "Age": 33, "Speed": 6, "Job": "Singer"},
    {"Name": "Liam", "Age": 31, "Speed": 4, "Job": "Director"},
    {"Name": "Mia", "Age": 29, "Speed": 3, "Job": "Producer"},
    {"Name": "Alexander", "Age": 35, "Speed": 3, "Job": "Engineer"},
    {"Name": "Sophie", "Age": 32, "Speed": 4, "Job": "Doctor"},
    {"Name": "Benjamin", "Age": 28, "Speed": 3, "Job": "Teacher"},
    {"Name": "Emily", "Age": 30, "Speed": 4, "Job": "Nurse"},
    {"Name": "James", "Age": 45, "Speed": 6, "Job": "Lawyer"},
    {"Name": "Amelia", "Age": 27, "Speed": 4, "Job": "Architect"},
    {"Name": "Henry", "Age": 35, "Speed": 3, "Job": "Chef"},
    {"Name": "Jessica", "Age": 40, "Speed": 6, "Job": "Scientist"},
    {"Name": "Daniel", "Age": 29, "Speed": 4, "Job": "Photographer"},
    {"Name": "Antonio", "Age": 70, "Speed": 1, "Job": "Pensioner"},
    {"Name": "Sinty", "Age": 69, "Speed": 2, "Job": "Pensioner"},
    {"Name": "Avame", "Age": 18, "Speed": 9, "Job": "Programmer"},
    ]



async def sit_to_bus(info):
    try:
        await asyncio.sleep(info['Speed'])
        print(f'{info["Name"]} сел в автобус.')
        return info
    except asyncio.CancelledError:
        print(f'{info["Name"]} {info["Job"]} не успел/а вовремя сесть в автобус.')
        return info


async def main():
    tasks = [asyncio.create_task(sit_to_bus(info)) for info in passengers]
    try:
        results = await asyncio.wait_for(asyncio.gather(*tasks) , timeout=5)
    except asyncio.TimeoutError:
        pass

    # print('______________________________________')
    # done, pending = await asyncio.wait(tasks, timeout=5)
    # print(done)
    # print(pending)

asyncio.run(main())