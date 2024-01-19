
def greeting(name):                         # Определение функции приветствия, которая принимает имя в качестве аргумента
    return f"Привет, {name}!"


def farewell(name):                         # Определение функции прощания, которая принимает имя в качестве аргумента
    return f"Пока, {name}!"


def process_name(callback, name):           # Определение функции process_name, которая принимает callback-функцию и имя в качестве аргументов
    return callback(name)


name = "Студент"                            # Задаем имя "Студент"

result = process_name(greeting, name)       # Вызываем process_name с функцией приветствия и именем "Студент", результат записываем в переменную result
print(result)

result = process_name(farewell, name)       # Вызываем process_name с функцией прощания и именем "Студент", результат записываем в переменную result
print(result)