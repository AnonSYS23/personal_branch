print('Bienvenido a calendario')

option = int(input('Elija una opcion del 1 al 7 para continuar:'))
match option:
    case 1:
     print('Hoy es el dia lunes')    
    case 2:
     print('Hoy es el dia martes')
    case 3:
     print('Hoy es el dia miercoles')
    case 4:
     print('Hoy es el dia jueves')
    case 5:
     print('Hoy es el dia viernes')
    case 6:
     print('Hoy es el dia sabado')
    case 7:
     print('Hoy es el dia domingo') 
    case _:
     print('Error encontrado, vuelva a iniciar')   

