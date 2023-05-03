passwd = 'programmer'

print('Bienvenido, ingrese su contraseña para entrar')

passwd1 = str(input('Introduzca la contraseña :'))

while passwd != passwd1:
    passwd1 = str(input('Introduzca la contraseña denuevo :'))
print('Acceso concedido')