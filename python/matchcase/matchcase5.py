print('Bienvenido a calculadora LITE')

user = str(input('Ingrese su nombre aqui :'))
n1 = int(input(f'{user.capitalize()} ingrese un numero :'))
n2 = int(input(f'{user.capitalize()} Ingrese otro numero :'))

option = str(input(f'{user.capitalize()} que accion desea realizar, suma o resta :'))

user.capitalize()

match option:
    case 'suma':
        x = n1 + n2
        print(f'{user.capitalize()} la suma es : {x}')
    case 'resta':
        y = n1 - n2
        print(f'{user.capitalize()} la resta es : {y}')
