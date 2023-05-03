print('Bienvenido a Pizzerona')

user = str(input('Nombre del cliente :'))
price = float(input('Precio del producto solicitado :'))

menu = """
    Membresia del cliente:
1: Sin membresia
2: Basic
3: Medium
4: Premium
"""

print(menu)

member = int(input('Ingrese opcion :'))

match member:
    case 1:
        print('Su descuento es del 5%')
        x = price * 0.95
        print(f'{user} su descuento  es de {x}')
    case 2:
        print('Su descuento es del 10%')
        y = price * 0.90
        print(f'{user} su descuento total es de {y}')
    case 3:
        print('Su descuento es del 18%')
        z = price * 0.82
        print(f'{user} su descuento total es de {z}')
    case 4:
        print('Su descuento es del 25%')
        a = price * 0.75
        print(f'{user} su descuento total es de {a}')
    case _:
        print('Error, ingrese un numero valido')