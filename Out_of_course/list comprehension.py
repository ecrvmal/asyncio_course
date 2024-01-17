list_data = [1, 2, 3, 4]

digits = [x**2 for x in list_data]

print(digits)

def f(x):
    return x**2


squares = list(map(f, list_data))

print(f'{squares=}')

squares = list(map(lambda x: x**3 , list_data))

print(squares)
