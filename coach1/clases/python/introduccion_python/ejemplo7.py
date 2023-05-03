user = str(input('Cual es su nombre :'))
n1 = int(input('Agrege un numero aqui :'))
n2 = int(input('Agrege otro numero aqui :'))

user.capitalize()

if n1 > n2:
    print(f'{user.capitalize()} el numero {n1} es mayor')
    print(f'{user.capitalize()} el numero {n2} es menor')
elif n2 > n1:
    print(f'{user.capitalize()} el numero {n2} es mayor')
    print(f'{user.capitalize()} el numero {n1} es menor')  
else:
    print(f'{user.capitalize()} los numeros son iguales')          