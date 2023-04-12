print('Bienvenido a Calendario 1.1')

month = int(input('Inserte el mes que quiere ingresar del 1 al 12 :'))

match month:
    case 1:
        print('Enero')
    case 2:
        print('Febrero')
    case 3:
        print('Marzo')
    case 4:
        print('Abril')
    case 5:
        print('Mayo')
    case 6:
        print('Junio')
    case 7:
        print('Julio')
    case 8:
        print('Agosto')
    case 9:
        print('Septiembre')
    case 10:
        print('Octubre')
    case 11:
        print('Noviembre')
    case 12:
        print('Diciembre')
    case _:
        print('Mes invalido, intente mas tarde')