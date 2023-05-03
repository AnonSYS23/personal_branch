print('Bienvenido a Convertor MINI')

user = str(input('Ingrese su usuario aqui :'))
metros = float(input('Ingrese los metros que quiere convertir :'))

menu = """
  Unidades disponibles para convertir
1. Kilometros
2. Hectometros
3. Decametros
4. Decimetros
5. Centimetros
6. Milimetros
"""

print(menu)


opcion = int(input('ingrese opcion :'))

match opcion:
    case 1:
        x = metros * 1/1000
        print(f'Su convesion de metros a kilometros es {x}')
    case 2:
        y = metros * 1/100
        print(f'Su convesion de metros a hectometros es {y}')
    case 3:
        z = metros * 1/10
        print(f'Su convesion de metros a decametros es {z}')
    case 4:
        a = metros * 1/0.1
        print(f'Su convesion de metros a decimetros es {a}')
    case 5:
        b = metros * 100/1
        print(f'Su convesion de metros a centimetros es {b}')
    case 6:
        c = metros * 1000/1
        print(f'Su convesion de metros a milimetros es {c}')
    case _:
        print('Ingrese un numero valido')