user = str(input('Nombre del cliente :'))
clothes = int(input('Cantidad de camisas adquiridas :'))
price = int(input('Cantidad de dinero de los productos :'))

user.capitalize()

if clothes >= 3:
    x = price * 0.80
    print(f'{user.capitalize()} su descuento sera del 25%')
    print(f'{user.capitalize()} su transaccion es de {x}')
else:
    y = price * 0.90
    print(f'{user.capitalize()} su descuento sera del 10%')
    print(f'{user.capitalize()} su transaccion es de {y}')      
