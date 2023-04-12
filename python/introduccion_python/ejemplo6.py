user = str(input('Ingrese su usuario :'))
number = int(input('Ingrese un numero :'))

user.capitalize()

if number > 0:
    print(f'{user.capitalize()} Su numero es positivo')
elif number == 0:
    print(f'{user.capitalize()} su numero es neutro')
else:
    print(f'{user.capitalize()} su numero es negativo')    
