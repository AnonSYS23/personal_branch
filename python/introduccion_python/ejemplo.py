porciento1 = float(input('Inserte su nota porfavor :'))
porciento2 = float(input('Inserte su nota porfavor :'))
porciento3 = float(input('Inserte su nota porfavor :'))
porciento4 = float(input('Inserte su nota porfavor :'))

print('-' * 20)

name = input('Como te llamas en primer lugar :')
grade = input('Cual es tu semestre universitario :')
age = input('Cual es tu edad :')
confirmation = input('Estas listo para tu nota?')

name.lower()


x = porciento1 * 0.5
y = porciento2 * 0.25
z = porciento3 * 0.35
a = porciento4 * 0.15

total = x + y + z + a /4

print(f'{name.lower()} su nota final es : {total}')