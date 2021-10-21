import random
import numpy as np

def crear_album(figus_total):
	'''
	Devuelve un álbum vacío con figus_total espacios para pegar figuritas. El álbum se representa
	como un vector de ceros.
	'''
	album = np.zeros(figus_total)
	return album


def album_incompleto(A):
	'''
	Recibe un vector y devuelve True si el álbum A no está completo y False si está completo.
	'''
	album_incompleto = 0 in A
	return album_incompleto


def comprar_figu(figus_total):
	# Cada figu representa una posición del array del álbum, las etiquetamos como 0, 1, ..., (figus_total - 1).
	numero_figurita = random.randint(0, figus_total-1)
	return numero_figurita


def cuantas_figus(figus_total):
	album_nuevo = crear_album(figus_total)
	figus_compradas = 0
	while album_incompleto(album_nuevo):
		figu = comprar_figu(figus_total)
		figus_compradas += 1
		album_nuevo[figu] += 1
	#print(f'Hizo falta comprar {figus_compradas} figuritas para completar el álbum.')
	return figus_compradas


def experimento_figus(n_repeticiones, figus_total):
	resultados = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
	promedio_resultados = np.mean(resultados)
	return promedio_resultados

def comprar_paquete(figus_total, figus_paquete):
	# Cada figu representa una posición del array del álbum, las etiquetamos como 0, 1, ..., (figus_total - 1).
	paquete = [random.randint(0, figus_total-1) for figu in range(figus_paquete)]
	return paquete


def cuantos_paquetes(figus_total, figus_paquete):
	album_nuevo = crear_album(figus_total)
	paquetes_comprados = 0
	while album_incompleto(album_nuevo):
		paquete = comprar_paquete(figus_total, figus_paquete)
		paquetes_comprados += 1
		for figu in paquete:
			album_nuevo[figu] += 1
	#print(f'Hizo falta comprar {paquetes_comprados} paquetes para completar el álbum.')
	return paquetes_comprados


def main():
	print('Ejercicio 5.14')
	n_repeticiones = 1000
	figus_total = 6
	resultados = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
	promedio_resultados = np.mean(resultados)
	print(f'En promedio hace falta comprar {promedio_resultados} figuritas para completar un álbum de {figus_total} figuritas.')
	print('\nEjercicio 5.15')
	promedio = experimento_figus(100, 670)
	print(f'En promedio hace falta comprar {promedio} figuritas para completar un álbum de 670 figuritas.')
	print('\nEjercicio 5.19')
	# Quedó definido antes que n_repeticiones=1000, por eso no lo escribo acá
	figus_total = 670
	figus_paquete = 5
	resultados_paquete = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
	promedio_resultados_paquete = np.mean(resultados_paquete)
	print(f'En promedio hace falta comprar {promedio_resultados_paquete} paquetes para completar un álbum de {figus_total} figuritas.')


# >>> main()
# Ejercicio 5.14
# En promedio hace falta comprar 14.286 figuritas para completar un álbum de 6 figuritas.

# Ejercicio 5.15
# En promedio hace falta comprar 4898.76 figuritas para completar un álbum de 670 figuritas.

# Ejercicio 5.19
# En promedio hace falta comprar 948.348 paquetes para completar un álbum de 670 figuritas.