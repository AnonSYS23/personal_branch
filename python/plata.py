name = str(input('Ingrese su nombre aqui:'))
money = int(input('Inserte la cantidad de dinero que desea:'))
account = str(input('Inserte su tipo de cuenta:'))
age = int(input('Cual es su edad legalmente:'))

account1 = 'ahorro'

if age == 18:
    print(f'{name} Puedes retirar tu dinero sin problemas detectados')
if account != account1 and age >= 18:
    print('No has seleccionado la cuenta bancaria correctamente')
else:
    print('Se ha registrado un error en su transferencia')
