passwd = 'programmer'
counter = 0

print('Bienvenido, ingrese su contraseña para entrar')

passwd1 = str(input('Introduzca la contraseña :'))

while passwd != passwd1:
    passwd1 = str(input('Introduzca la contraseña denuevo :'))
    counter += 1
    if counter == 2:
        print('Acceso bloqueado a la cuenta')
        break
    elif passwd == passwd1:
        print('Acceso concedido')
        break