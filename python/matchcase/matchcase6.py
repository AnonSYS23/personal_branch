print('Bienvenido a Royal Flims')

user = str(input('Ingrese el nombre del cliente :'))
total = float(input('Ingrese el precio de la pelicula :'))

menu="""
    metodos de pago:
opcion 1 = efectivo
opcion 2 = tarjeta credito/debito
option 3 = tarjeta royal flims

"""
print(menu)
opcion =int(input(f'{user} marque opcion: '))
match opcion:
    case 1:
        print('Tienes un descuento de 10%')
        x = total * 0.10
        print(f'{user} El precio de la pelicula es de {total} y se le resta {x} pesos')
    case 2:
        print(' Tienes un descuento del 15%')
        y = total * 0.15
        print(f'{user} El precio de la pelicula es de {total} y se le resta {y} pesos')
    case 3:
        print('Tienes un descuento del 20%')
        z = total * 0.20
        print(f'{user} El precio de la pelicula es de {total} y se le resta {z} pesos')
    case _:
        print('Error, vuelve a intentar')

print('Gracias por estar en nuestros cines Royal Flims')