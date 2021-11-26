def burbuja(lista, i):
	'''Ejecuta paso elemental de ord_burbujeo.'''
    if lista[i] > lista[i + 1]:
        lista.insert(i, lista.pop(i + 1))	 
	

def ord_burbujeo(lista):
	'''Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''
    for L in range(len(lista) - 1, 0, -1):
        for i in range(L):
            burbuja(lista, i)
    return lista


# Las comparaciones que hace la función en una lista de largo n son
# (n-1) + (n-2) + ... = (n-1) n / 2 ~ n**2