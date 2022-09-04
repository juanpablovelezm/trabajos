notas = []
porcentajes = []
totalporcentaje = 0
notaFinal = 0

limit = int(input('Ingresa el numero de notas que vas a ingresar: '))

for i in range(limit):
  nota = float(input(f"\nIngresa la nota {i+1}/{limit}: "))
  notas.append(nota)

  if i == limit - 1:
    print(f'\nUltimo porcentaje se define automaticamente en {100 - totalporcentaje}%')
    porcentaje = 100 - totalporcentaje

  else:
    porcentaje = float(input(f"Ingresa el porcentaje que vale la nota: "))

    while porcentaje + totalporcentaje > 100:
      porcentaje = float(input(f"\nLa suma de los porcentajes no puede ser mayor a 100, ingresa otro porcentaje que no sea mayor al {100 - totalporcentaje}%: "))
    
    porcentajes.append(porcentaje)
    totalporcentaje += porcentaje


for i in range(len(notas)):
  notaFinal += notas[i-1] * porcentajes[i-1] / 100

print(f"Nota final: {round(notaFinal, 2)}")