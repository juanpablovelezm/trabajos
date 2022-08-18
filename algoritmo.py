lista_notas = []
lista_porcentajes = []
porcetaje_total = 0
notaFinal = 0
suma_notas = 0

contador = 0
print('\nVamos a calcular el promedio de tus notas')

''' bucle '''
while True: #while es un bucle y true significa verdadero
  #toma la nota que ingresa y la inserta en la lista
  nota = float(input(f"\nIngresa una nota: "))
  lista_notas.append(nota) #append inserta un valor a la lista

  print(f"\nlista de notas => {lista_notas}")

  #toma el porcentaje de la nota y lo inserta en la lista
  porcentaje = float(input(f"\nIngresa el porcentaje de la nota: "))
  lista_porcentajes.append(porcentaje) #append inserta un valor a la lista

  #suma los porcentajes de la lista
  porcetaje_total += porcentaje

  print(f"\nlista de porcentajes => {lista_porcentajes}")
  print(f"Suma de porcentajes => {porcetaje_total}")

  #pregunta si quiere seguir ingresando lista_notas
  print('\n-------------------------------------------------')
  continuar = input('\n"Y" para ingresar otra nota: ').lower()
  if continuar != "y":
    break #break detiene el ciclo


#reduce o aumenta para que sumen en total 100%

#si el porcentaje total es mayor a 100%
''' condincionales '''
if porcetaje_total > 100:
  #calcula el porcentaje que sobra
  porcentaje_Diff = (porcetaje_total - 100) / len(lista_porcentajes)

  #y lo resta a los porcentajes de la lista
  for i in range(len(lista_porcentajes)):
    lista_porcentajes[i] -= porcentaje_Diff

#si el porcentaje total es menor a 100%
elif porcetaje_total < 100:
#calcula el porcentaje que falta para llegar a 100%
  porcentaje_Diff = (100 - porcetaje_total) / len(lista_porcentajes)
  
  #y lo suma a los porcentajes de la lista
  for i in range(len(lista_porcentajes)): #es un bucle, se le indica cuantas veces se ejecuta

    #i me indica en que posicion va el ciclo
    lista_porcentajes[i] += porcentaje_Diff

print(f"porcentajes finales =>{lista_porcentajes}")


''' bucle '''
for i in range(len(lista_porcentajes)):
  notaFinal += (lista_notas[i] * lista_porcentajes[i]) / 100
  #print(round(notaFinal, 3), ' ', lista_notas[i], ' ', lista_porcentajes[i])

print(f"\nEl promedio de tus notas es: {round(notaFinal,1)}")
