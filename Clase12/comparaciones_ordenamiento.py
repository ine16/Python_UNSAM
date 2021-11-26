from random import randint
import numpy as np
import matplotlib.pyplot as plt

def generar_lista(N):
	'''Genera lista de largo N con números aleatorios del 1 al 1000 
	   con repeticiones'''
    lista = [randint(1, 1000) for _ in range(N)]
    return lista

#%%

def burbuja(lista, i):
    if lista[i] > lista[i + 1]:
        lista.insert(i, lista.pop(i + 1))
    return 1

def ord_burbujeo(lista):
    contador = 0
    for L in range(len(lista) - 1, 0, -1):
        for i in range(L):
            contador += burbuja(lista, i)
    return contador

#%%

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # variable que va a contar las comparaciones
    contador = 0

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento y num de comparaciones
        p, aux_contador = buscar_max(lista, 0, n)

        contador += aux_contador

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1
    
    return contador

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    # variable que va a contar las comparaciones
    contador = 0

    pos_max = a
    for i in range(a + 1, b + 1):
        contador += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, contador

#%%

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    contador = 0

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        contador += 1
        if lista[i + 1] < lista[i]:
            contador += reubicar(lista, i + 1)
            #reubicar(lista, i + 1)
        

    return contador

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    contador = 1

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        contador += 1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

    return contador

#%%

def experimento(N, k, incluye_merge = False):
    '''Repite k veces lo siguiente:
	   genera una lista de largo N, ordena la lista con los tres métodos 
	   y guarda la cantidad de operaciones.
	   Pre: N y k deben ser enteros positivos
	   Post: Devuelve tupla con el promedio de comparaciones de cada método''' 

    contador_burbujeo = 0
    contador_insercion = 0
    contador_seleccion = 0
    if incluye_merge:
         contador_merge = 0

    for i in range(k):
        lista = generar_lista(N)
        contador_burbujeo += ord_burbujeo(lista.copy())
        contador_insercion += ord_insercion(lista.copy())
        contador_seleccion += ord_seleccion(lista.copy())
        if incluye_merge:
            contador_merge += merge_sort(lista.copy())[1]

    if incluye_merge:
    	return (contador_burbujeo/k, contador_insercion/k, 
    		    contador_seleccion/k, contador_merge/k)
    return (contador_burbujeo/k, contador_insercion/k, contador_seleccion/k)

#%%


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comparaciones, aux_comparaciones_izq, aux_comparaciones_der = 0, 0, 0

    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, aux_comparaciones_izq = merge_sort(lista[:medio])
        der, aux_comparaciones_der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
        comparaciones += 1 + aux_comparaciones_izq + aux_comparaciones_der
    return lista_nueva, comparaciones

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

#%%

def experimento_vectores(Nmax):
    '''Para N entre 1 y Nmax genera una lista de largo N con números enteros
       del 1 al 1000 en orden aleatorio, calcula la cantidad de comparaciones
       realizadas por cada método de ordenamiento y guarda estos resultados 
       en tres vectores de largo Nmax'''

    comparaciones_seleccion = np.zeros(Nmax)
    comparaciones_insercion = np.zeros(Nmax)
    comparaciones_burbujeo = np.zeros(Nmax)
    comparaciones_merge = np.zeros(Nmax)

    for N in range(Nmax):
        comparaciones_burbujeo[N], comparaciones_insercion[N], \
    	    comparaciones_seleccion[N], comparaciones_merge[N] \
    	    = experimento(N = N + 1, k = 1000, incluye_merge = True)


    largos = np.arange(1, Nmax + 1)
    plt.plot(largos, comparaciones_seleccion, 'bo', label = "seleccion")
    plt.plot(largos, comparaciones_insercion, label = "insercion")
    plt.plot(largos, comparaciones_burbujeo, label = "burbujeo")
    plt.plot(largos, comparaciones_merge, label = "merge sort")

    plt.legend()
    plt.show()

