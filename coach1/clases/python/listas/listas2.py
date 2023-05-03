materias = ['Sociales','Español','Ingles','Matematica','Quimica','Fisica']
notas = []
for i in materias:
    nota = float(input(f'Cual es tu nota en {i}?'))
    notas.append(nota)
for i in range(len(materias)):
    print(f'Tu nota en {materias[i]} es {notas[i]}')
