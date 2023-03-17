# Programa en python para hacer una calculadora simple
# Tomando la entrada del usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("Operación: +, -, *, /")
seleccion = input("Seleccione la operacion necesaria: ")
if seleccion == "+":
  print(num1, "+", num2, "=", num1+num2)
elif seleccion == "-":
  print(num1, "-", num2, "=", num1-num2)
elif seleccion == "*":
  print(num1, "*", num2, "=", num1*num2)
elif seleccion == "/":
  print(num1, "/", num2, "=", num1/num2)
else:
  print("Entrada invalida por el sistema")