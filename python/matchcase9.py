print('Bienvenido a Revisador de notas 1.0')

user = str(input('Ingrese el usuario de administrador :'))


menu = """
 Selecciona la nota del estudiante:
5. Excelente
4. Buena
3. Regular
2. Suficiente
1. No suficiente
"""

print(menu)

note = int(input(f'{user} Selecciona la nota correcta segun el estudiante del 1 al 5 :'))

match note:
    case 5:
        print('La nota del estudiante es Excelente')
    case 4:
        print('La nota del estudiante es Buena')
    case 3:
        print('La nota del estudiante es Regular')
    case 2:
        print('La nota del estudiante es Suficiente')
    case 1:
        print('La nota del estudiante es No Suficiente')
    case _:
        print('La nota del estudiante es incorrecta')
