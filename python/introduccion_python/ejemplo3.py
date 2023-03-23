#crea un algoritmo que le pida al estudiante su nombre, edad, carrera universitaria 
#donde al final del programa le imprima si puede entrar a la universidad o no 
#[la edad minima es 20 y debe imprimir con la letra inicial de su nombre en mayuscula]

name = str(input('Cual es su nombre : '))
age = int(input('Cual es su edad :'))
Career = str(input('Cual es su carrera universitaria'))

name.capitalize()


if age == 18:
    print(f'{name.capitalize()}Puedes tener una oportunidad de estudiar con nosotros')
elif age >= 18:
    print(f'{name.capitalize()}Puedes hacer una prueba para comprobar sus conocimientos')    
else:
    print(f'{name.capitalize()}No puedes ser aceptado en la institucion de educacion superior')    