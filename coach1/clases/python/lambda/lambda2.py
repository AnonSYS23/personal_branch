from functools import reduce

def add(a, b):
    return a + b

print(reduce(add, [1, 2, 3, 4]))  # 10

def doblar(numero):
    return numero*2

numeros = [2, 5, 10, 23, 50, 33]

map(doblar, numeros)

def multiple(numero):    # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True      # Sólo devolvemos True si lo es

numeros = [2, 5, 10, 23, 50, 33]

filter(multiple, numeros)