num = int(input('Ingrese un numero par :'))
for i in range(1, num+1):
    if i % 2 != 0:
        print(i, end="-")