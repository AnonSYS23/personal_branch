print('Bienvenido a convertor LITE')

user = str(input('Como se llama usted :'))

convertor = lambda money : money * 5000
convertor1 = lambda money : money * 256
convertor2 = lambda money : money * 23
convertor3 = lambda money : money * 208
convertor4 = lambda money : money * 792
convertor5 = lambda money : money * 54
convertor6 = lambda money : money * 38
convertor7 = lambda money : money * 7
convertor8 = lambda money : money * 5
convertor9 = lambda money : money * 5

money = float(input('Introduzca los dolares que quiere ingresar :'))
option = str(input('Elija a que moneda quiere recibir desde el a hasta la j :'))

a = convertor(money * 5000)
b = convertor1(money * 256)
c = convertor2(money * 23)
d = convertor3(money * 208)
e = convertor4(money * 792)
f = convertor5(money * 54)
g = convertor6(money * 38)
h = convertor7(money * 7)
i = convertor8(money * 5)
j = convertor9(money * 5)

if option == 'a':
    print('El valor de la moneda es :', money * 5000)
if option == 'b':
    print('El valor de la moneda es :', money * 256)
if option == 'c':
    print('El valor de la moneda es :', money * 23)
if option == 'd':
    print('El valor de la moneda es :', money * 208)
if option == 'e':
    print('El valor de la moneda es :', money * 792)
if option == 'f':
    print('El valor de la moneda es :', money * 54)
if option == 'g':
    print('El valor de la moneda es :', money * 38)
if option == 'h':
    print('El valor de la moneda es :', money * 7)
if option == 'i':
    print('El valor de la moneda es :', money * 5)
if option == 'j':
    print('El valor de la moneda es :', money * 5)