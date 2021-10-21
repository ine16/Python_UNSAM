import random
from collections import Counter

def cumple_repetido(personas):
	hay_cocumple = False
	lista_cumples = [random.randint(1,365) for i in range(personas)]
	#print(lista_cumples)
	dicc_repeticiones = Counter(lista_cumples)
	dia_repetido = max(dicc_repeticiones, key=dicc_repeticiones.get)
	#print(dia_repetido)
	# Con que hayan 2 personas que cumplan el mismo dia ya estoy en este caso
	if dicc_repeticiones[dia_repetido] >= 2:
		hay_cocumple = True
	return hay_cocumple


def mas_probable_cumple_repetido():
	# Número inicial de personas que considero
	N = 2
	G_repetidos = sum([cumple_repetido(N) for i in range(10000)])
	prob_2_cumples_repetidos = G_repetidos / 10000

	while prob_2_cumples_repetidos <= 0.5:
		N += 1
		G_repetidos = sum([cumple_repetido(N) for i in range(10000)])
		prob_2_cumples_repetidos = G_repetidos / 10000
	return N

# Respuesta a la pregunta: si hay al menos 23 personas ya es más probable que 2 cumplan años el mismo día a que todas
#cumplan en días distintos
# >>> mas_probable_cumple_repetido()
# 23
# >>> mas_probable_cumple_repetido()
# 23