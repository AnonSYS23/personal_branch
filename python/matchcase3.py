user = str(input('Ingrese su nombre aca porfavor :'))
number = float(input("Escribe un numero aqui porfavor :"))
user.capitalize()

if number > 0:
    print(f"{user.capitalize()} su numero es positivo")
elif number < 0:
    print(f"{user.capitalize()} su numero es negativo")
else:
    print(f"{user.capitalize()} su numero es neutro")