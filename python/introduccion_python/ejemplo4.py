#Escribe un programa que pregunte al usuario un número y el programa diga si es un número par o un número impar
user = str(input('Introduzca su nombre aqui :'))
number = int(input('Introduzca un numero porfavor :'))

user.capitalize()

if number == 0:
    print(f'{user.capitalize()} su numero es neutro')
elif number %2 == 0:
    print(f'{user.capitalize()} su numero es par')
else:
    print(f'{user.capitalize()} su numero es impar')
